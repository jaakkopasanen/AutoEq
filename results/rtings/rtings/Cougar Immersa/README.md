# Cougar Immersa

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 0.0; 23 2.2; 25 1.6; 28 0.6; 31 -0.3; 34 -1.0; 37 -1.6; 41 -2.4; 45 -3.1; 49 -3.7; 54 -4.4; 60 -5.1; 66 -6.1; 72 -7.0; 79 -8.0; 87 -9.0; 96 -9.8; 106 -10.4; 116 -10.8; 128 -11.1; 141 -11.2; 155 -11.1; 170 -10.9; 187 -10.5; 206 -10.1; 227 -9.6; 249 -9.1; 274 -8.7; 302 -8.4; 332 -7.8; 365 -7.1; 402 -6.1; 442 -5.0; 486 -4.2; 535 -3.4; 588 -2.6; 647 -1.8; 712 -1.4; 783 -1.2; 861 -0.9; 947 -0.4; 1042 0.5; 1146 1.9; 1261 3.0; 1387 3.0; 1526 3.0; 1678 2.5; 1846 0.8; 2031 -1.0; 2234 -1.0; 2457 -0.0; 2703 0.8; 2973 0.9; 3270 0.1; 3597 -1.6; 3957 -2.7; 4353 -2.9; 4788 0.0; 5267 0.7; 5793 1.5; 6373 -0.9; 7010 -0.5; 7711 -1.6; 8482 -4.8; 9330 -6.8; 10263 -4.3; 11289 -0.4; 12418 0.0; 13660 0.0; 15026 -0.3; 16529 -0.9; 18182 -0.0; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cougar Immersa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cougar Immersa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.98 | 4.3 dB   |
| Peaking | 132 Hz  | 0.54 | -11.0 dB |
| Peaking | 318 Hz  | 1.2  | -3.1 dB  |
| Peaking | 1359 Hz | 2.56 | 4.1 dB   |
| Peaking | 9328 Hz | 3.89 | -7.4 dB  |
| Peaking | 662 Hz  | 6.07 | 0.4 dB   |
| Peaking | 2183 Hz | 4.44 | -2.9 dB  |
| Peaking | 2846 Hz | 1.16 | 2.1 dB   |
| Peaking | 4141 Hz | 2.39 | -5.4 dB  |
| Peaking | 5135 Hz | 3.11 | 3.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Cougar%20Immersa/Cougar%20Immersa.png)