# AKG K3003

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.4; 23 -3.5; 25 -3.6; 28 -3.6; 31 -3.6; 34 -3.5; 37 -3.5; 41 -3.6; 45 -3.8; 49 -3.9; 54 -4.1; 60 -4.2; 66 -4.5; 72 -4.7; 79 -5.1; 87 -5.4; 96 -5.7; 106 -6.0; 116 -6.2; 128 -6.4; 141 -6.5; 155 -6.6; 170 -6.6; 187 -6.5; 206 -6.4; 227 -6.2; 249 -5.9; 274 -5.6; 302 -5.3; 332 -4.9; 365 -4.5; 402 -4.0; 442 -3.6; 486 -3.1; 535 -2.6; 588 -2.1; 647 -1.6; 712 -1.1; 783 -0.6; 861 -0.2; 947 -0.0; 1042 -0.0; 1146 -0.1; 1261 -0.1; 1387 -0.2; 1526 0.1; 1678 0.6; 1846 1.1; 2031 1.4; 2234 1.8; 2457 2.6; 2703 3.3; 2973 2.5; 3270 5.2; 3597 6.0; 3957 6.0; 4353 5.6; 4788 0.2; 5267 -1.5; 5793 -2.8; 6373 -2.1; 7010 -3.6; 7711 -5.7; 8482 -3.7; 9330 -0.3; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.9; 15026 -4.2; 16529 -0.4; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.15 | -3.1 dB |
| Peaking | 158 Hz   | 0.66 | -4.4 dB |
| Peaking | 339 Hz   | 0.99 | -2.4 dB |
| Peaking | 4007 Hz  | 1.29 | 12.6 dB |
| Peaking | 5511 Hz  | 0.92 | -9.1 dB |
| Peaking | 2478 Hz  | 7.81 | 0.5 dB  |
| Peaking | 6681 Hz  | 4.8  | 4.4 dB  |
| Peaking | 7646 Hz  | 2.11 | -6.6 dB |
| Peaking | 9447 Hz  | 1.49 | 4.5 dB  |
| Peaking | 14900 Hz | 4.29 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/AKG%20K3003/AKG%20K3003.png)