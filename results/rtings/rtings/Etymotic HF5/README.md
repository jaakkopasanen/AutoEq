# Etymotic HF5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.8; 106 4.9; 116 4.0; 128 3.1; 141 2.3; 155 1.6; 170 1.1; 187 0.6; 206 0.2; 227 -0.1; 249 -0.1; 274 -0.2; 302 -0.3; 332 -0.3; 365 -0.4; 402 -0.4; 442 -0.3; 486 -0.3; 535 -0.1; 588 0.1; 647 0.4; 712 0.7; 783 0.8; 861 0.7; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.9; 1387 -2.5; 1526 -2.9; 1678 -3.4; 1846 -3.8; 2031 -4.0; 2234 -3.4; 2457 -2.3; 2703 -1.5; 2973 -1.1; 3270 -1.0; 3597 -1.2; 3957 -1.7; 4353 -1.7; 4788 -0.3; 5267 2.5; 5793 5.1; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic HF5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic HF5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.47 | 6.9 dB  |
| Peaking | 853 Hz  | 3.17 | 1.6 dB  |
| Peaking | 1838 Hz | 1.28 | -4.0 dB |
| Peaking | 4303 Hz | 4.32 | -2.2 dB |
| Peaking | 6037 Hz | 3.65 | 6.4 dB  |
| Peaking | 16 Hz   | 1.15 | 2.4 dB  |
| Peaking | 43 Hz   | 1.11 | -1.4 dB |
| Peaking | 94 Hz   | 2.03 | 2.1 dB  |
| Peaking | 232 Hz  | 0.99 | -1.3 dB |
| Peaking | 8078 Hz | 5.85 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Etymotic%20HF5/Etymotic%20HF5.png)