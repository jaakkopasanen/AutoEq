# AKG K701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.2; 34 4.7; 37 4.4; 41 4.0; 45 3.6; 49 3.3; 54 3.0; 60 2.7; 66 2.5; 72 2.3; 79 2.1; 87 1.8; 96 1.5; 106 1.1; 116 0.7; 128 0.3; 141 -0.0; 155 -0.2; 170 -0.3; 187 -0.5; 206 -0.6; 227 -0.6; 249 -0.5; 274 -0.5; 302 -0.4; 332 -0.3; 365 -0.2; 402 -0.2; 442 -0.2; 486 0.1; 535 0.8; 588 1.5; 647 1.5; 712 1.7; 783 1.4; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.4; 1526 -2.3; 1678 -3.6; 1846 -4.9; 2031 -5.6; 2234 -6.4; 2457 -5.8; 2703 -4.7; 2973 -3.0; 3270 -1.2; 3597 0.2; 3957 -0.4; 4353 -1.4; 4788 -1.2; 5267 -0.7; 5793 -1.3; 6373 -3.6; 7010 -4.5; 7711 -5.3; 8482 -6.9; 9330 -4.8; 10263 -1.2; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.83 | 6.1 dB  |
| Peaking | 68 Hz    | 1.88 | 1.4 dB  |
| Peaking | 714 Hz   | 2.58 | 2.1 dB  |
| Peaking | 2184 Hz  | 2    | -6.7 dB |
| Peaking | 8191 Hz  | 2.64 | -6.9 dB |
| Peaking | 2678 Hz  | 7.51 | -1.1 dB |
| Peaking | 3622 Hz  | 6.53 | 2.0 dB  |
| Peaking | 6576 Hz  | 9.07 | -1.6 dB |
| Peaking | 11452 Hz | 3.41 | 1.2 dB  |
| Peaking | 18652 Hz | 4.37 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AKG%20K701/AKG%20K701.png)