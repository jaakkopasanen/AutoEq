# Cougar Immersa

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 21 0.0; 23 2.5; 25 1.8; 28 0.7; 31 -0.2; 34 -1.0; 37 -1.7; 41 -2.6; 45 -3.4; 49 -4.0; 54 -4.7; 60 -5.4; 66 -6.2; 72 -7.0; 79 -7.8; 87 -8.6; 96 -9.3; 106 -9.9; 116 -10.3; 128 -10.6; 141 -10.7; 155 -10.5; 170 -10.3; 187 -10.0; 206 -9.6; 227 -9.1; 249 -8.5; 274 -8.0; 302 -7.6; 332 -6.9; 365 -6.1; 402 -5.0; 442 -3.8; 486 -3.0; 535 -2.2; 588 -1.5; 647 -0.7; 712 -0.5; 783 -0.7; 861 -0.7; 947 -0.4; 1042 0.5; 1146 2.1; 1261 3.3; 1387 3.0; 1526 2.6; 1678 2.1; 1846 0.8; 2031 -0.6; 2234 -0.5; 2457 0.4; 2703 1.4; 2973 2.0; 3270 1.9; 3597 0.6; 3957 -1.5; 4353 -2.9; 4788 -0.1; 5267 1.2; 5793 3.0; 6373 1.7; 7010 2.0; 7711 -0.4; 8482 -4.4; 9330 -5.3; 10263 -1.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cougar Immersa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cougar Immersa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.51 | 4.4 dB   |
| Peaking | 125 Hz  | 0.56 | -10.1 dB |
| Peaking | 280 Hz  | 1.18 | -3.3 dB  |
| Peaking | 1343 Hz | 2.2  | 3.8 dB   |
| Peaking | 9050 Hz | 6.46 | -6.5 dB  |
| Peaking | 641 Hz  | 5.23 | 1.0 dB   |
| Peaking | 2131 Hz | 5.66 | -1.8 dB  |
| Peaking | 3122 Hz | 2.81 | 2.3 dB   |
| Peaking | 4277 Hz | 4.82 | -4.1 dB  |
| Peaking | 5947 Hz | 2.93 | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Cougar%20Immersa/Cougar%20Immersa.png)