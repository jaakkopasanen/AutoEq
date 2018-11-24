# Sennheiser Amperior

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.2; 28 3.5; 31 2.8; 34 2.2; 37 1.6; 41 0.8; 45 0.1; 49 -0.5; 54 -0.9; 60 -1.0; 66 -0.2; 72 -1.1; 79 -3.2; 87 -4.1; 96 -4.3; 106 -4.7; 116 -5.4; 128 -5.7; 141 -5.8; 155 -5.8; 170 -5.3; 187 -5.2; 206 -5.1; 227 -4.6; 249 -3.0; 274 -1.9; 302 -1.7; 332 -0.7; 365 0.7; 402 1.6; 442 1.7; 486 1.6; 535 1.5; 588 1.5; 647 1.3; 712 1.1; 783 0.9; 861 0.7; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -1.1; 1387 -1.8; 1526 -2.7; 1678 -3.9; 1846 -4.2; 2031 -4.3; 2234 -3.6; 2457 -2.3; 2703 -0.5; 2973 0.5; 3270 1.0; 3597 0.8; 3957 0.3; 4353 0.9; 4788 -0.1; 5267 -0.3; 5793 3.5; 6373 5.5; 7010 2.5; 7711 0.1; 8482 -5.1; 9330 -3.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Amperior GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.3  | 5.6 dB  |
| Peaking | 139 Hz  | 1.05 | -6.5 dB |
| Peaking | 1895 Hz | 2.7  | -4.9 dB |
| Peaking | 6339 Hz | 4.71 | 6.4 dB  |
| Peaking | 8665 Hz | 6.01 | -6.4 dB |
| Peaking | 33 Hz   | 2.45 | 0.5 dB  |
| Peaking | 224 Hz  | 3.47 | -2.2 dB |
| Peaking | 497 Hz  | 1.1  | 2.5 dB  |
| Peaking | 2680 Hz | 0.83 | -1.2 dB |
| Peaking | 3287 Hz | 2.43 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)