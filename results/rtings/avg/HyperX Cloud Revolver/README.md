# HyperX Cloud Revolver

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 -1.0; 23 -1.3; 25 -1.4; 28 -1.6; 31 -1.7; 34 -1.8; 37 -1.8; 41 -1.9; 45 -2.1; 49 -2.3; 54 -2.6; 60 -3.1; 66 -3.4; 72 -3.6; 79 -3.8; 87 -4.0; 96 -4.1; 106 -4.1; 116 -4.1; 128 -4.1; 141 -3.9; 155 -3.7; 170 -3.4; 187 -3.0; 206 -2.5; 227 -1.9; 249 -1.4; 274 -1.1; 302 -0.9; 332 -0.2; 365 0.2; 402 0.1; 442 -0.1; 486 0.3; 535 0.7; 588 1.0; 647 1.0; 712 1.0; 783 1.3; 861 0.9; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -1.9; 1526 -2.9; 1678 -4.7; 1846 -5.4; 2031 -5.1; 2234 -3.7; 2457 -2.1; 2703 -1.5; 2973 -1.1; 3270 0.7; 3597 3.6; 3957 4.5; 4353 3.4; 4788 2.6; 5267 2.1; 5793 2.5; 6373 2.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.5; 10263 -0.7; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.7; 18182 -4.9; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Revolver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Revolver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 75 Hz    | 0.75 | -3.4 dB |
| Peaking | 150 Hz   | 1.51 | -2.5 dB |
| Peaking | 1957 Hz  | 2.06 | -6.2 dB |
| Peaking | 4266 Hz  | 1.48 | 4.3 dB  |
| Peaking | 18413 Hz | 1.79 | -5.4 dB |
| Peaking | 709 Hz   | 1.59 | 1.6 dB  |
| Peaking | 3680 Hz  | 1.87 | -2.9 dB |
| Peaking | 3755 Hz  | 4.6  | 4.5 dB  |
| Peaking | 6607 Hz  | 5.98 | 2.5 dB  |
| Peaking | 9384 Hz  | 6.09 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Revolver/HyperX%20Cloud%20Revolver.png)