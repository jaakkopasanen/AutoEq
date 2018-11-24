# Cowin E7 Wired NC off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 4.8; 31 3.4; 34 2.1; 37 1.0; 41 -0.2; 45 -1.3; 49 -2.1; 54 -2.7; 60 -2.8; 66 -3.0; 72 -3.9; 79 -5.3; 87 -6.9; 96 -8.3; 106 -9.5; 116 -9.9; 128 -10.8; 141 -11.9; 155 -12.1; 170 -11.9; 187 -12.8; 206 -12.4; 227 -11.6; 249 -10.7; 274 -9.3; 302 -7.9; 332 -6.7; 365 -5.7; 402 -5.0; 442 -3.5; 486 -2.7; 535 -1.8; 588 -0.8; 647 -0.4; 712 -0.4; 783 0.0; 861 -0.2; 947 -0.0; 1042 -0.1; 1146 -0.6; 1261 -0.2; 1387 0.2; 1526 0.9; 1678 0.9; 1846 1.8; 2031 2.5; 2234 3.6; 2457 5.1; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.2; 4353 -0.2; 4788 -4.1; 5267 -4.2; 5793 -3.8; 6373 -4.8; 7010 -5.0; 7711 -2.7; 8482 -1.6; 9330 -1.9; 10263 -2.0; 11289 -1.6; 12418 -1.3; 13660 -2.0; 15026 -1.1; 16529 -0.7; 18182 -3.8; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 Wired NC off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Wired NC off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.54 | 7.1 dB   |
| Peaking | 127 Hz  | 0.79 | -7.9 dB  |
| Peaking | 223 Hz  | 1.02 | -8.0 dB  |
| Peaking | 3579 Hz | 1.07 | 16.6 dB  |
| Peaking | 4904 Hz | 0.86 | -13.9 dB |
| Peaking | 72 Hz   | 5.48 | 1.0 dB   |
| Peaking | 678 Hz  | 2.37 | 1.2 dB   |
| Peaking | 1367 Hz | 1.16 | -1.1 dB  |
| Peaking | 2639 Hz | 2.61 | 1.6 dB   |
| Peaking | 3248 Hz | 6.14 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cowin%20E7%20Wired%20NC%20off/Cowin%20E7%20Wired%20NC%20off.png)