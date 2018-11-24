# Sennheiser HD 800 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 5.4; 25 5.1; 28 4.8; 31 4.5; 34 4.3; 37 4.1; 41 3.8; 45 3.5; 49 3.3; 54 3.0; 60 2.6; 66 2.3; 72 2.1; 79 1.8; 87 1.5; 96 1.1; 106 0.6; 116 0.2; 128 -0.2; 141 -0.6; 155 -0.8; 170 -1.0; 187 -1.1; 206 -1.1; 227 -1.1; 249 -1.1; 274 -1.0; 302 -0.9; 332 -0.8; 365 -0.7; 402 -0.6; 442 -0.5; 486 -0.5; 535 -0.4; 588 -0.3; 647 -0.2; 712 -0.0; 783 -0.1; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.6; 1261 0.9; 1387 0.8; 1526 0.9; 1678 0.9; 1846 0.2; 2031 -0.3; 2234 0.6; 2457 1.3; 2703 2.6; 2973 2.7; 3270 3.9; 3597 2.5; 3957 1.1; 4353 1.4; 4788 2.3; 5267 2.5; 5793 1.2; 6373 -0.3; 7010 0.8; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.6  | 5.0 dB  |
| Peaking | 56 Hz   | 0.42 | 2.2 dB  |
| Peaking | 172 Hz  | 0.7  | -2.1 dB |
| Peaking | 3148 Hz | 2.77 | 3.6 dB  |
| Peaking | 5027 Hz | 5.05 | 2.4 dB  |
| Peaking | 1477 Hz | 2.21 | 1.0 dB  |
| Peaking | 2037 Hz | 4.56 | -1.4 dB |
| Peaking | 2277 Hz | 4.16 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)