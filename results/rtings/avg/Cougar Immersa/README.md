# Cougar Immersa

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 0.0; 23 2.2; 25 1.6; 28 0.6; 31 -0.3; 34 -1.0; 37 -1.6; 41 -2.4; 45 -3.1; 49 -3.7; 54 -4.4; 60 -5.1; 66 -6.1; 72 -7.0; 79 -8.0; 87 -9.0; 96 -9.8; 106 -10.4; 116 -10.8; 128 -11.1; 141 -11.2; 155 -11.1; 170 -10.9; 187 -10.5; 206 -10.1; 227 -9.6; 249 -9.1; 274 -8.7; 302 -8.4; 332 -7.8; 365 -7.1; 402 -6.1; 442 -5.0; 486 -4.2; 535 -3.4; 588 -2.6; 647 -1.8; 712 -1.4; 783 -1.2; 861 -0.9; 947 -0.4; 1042 0.5; 1146 1.9; 1261 3.0; 1387 3.0; 1526 3.0; 1678 2.5; 1846 0.8; 2031 -1.0; 2234 -1.0; 2457 -0.0; 2703 0.6; 2973 0.4; 3270 -0.6; 3597 -2.6; 3957 -3.9; 4353 -4.2; 4788 -1.8; 5267 -1.8; 5793 -1.0; 6373 -2.1; 7010 -1.1; 7711 -2.0; 8482 -3.9; 9330 -4.1; 10263 -2.1; 11289 -1.1; 12418 -1.0; 13660 -1.2; 15026 -2.8; 16529 -3.9; 18182 -4.3; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cougar Immersa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cougar Immersa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.56 | 3.8 dB   |
| Peaking | 128 Hz   | 0.65 | -10.9 dB |
| Peaking | 303 Hz   | 1.29 | -4.4 dB  |
| Peaking | 7227 Hz  | 0.76 | -2.4 dB  |
| Peaking | 20404 Hz | 0.74 | -7.4 dB  |
| Peaking | 1381 Hz  | 2.65 | 4.1 dB   |
| Peaking | 2924 Hz  | 5.73 | 1.5 dB   |
| Peaking | 4052 Hz  | 3.73 | -3.8 dB  |
| Peaking | 8356 Hz  | 1.11 | 2.8 dB   |
| Peaking | 8973 Hz  | 3.31 | -4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cougar%20Immersa/Cougar%20Immersa.png)