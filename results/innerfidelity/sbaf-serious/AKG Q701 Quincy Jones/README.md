# AKG Q701 Quincy Jones

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.4; 37 4.9; 41 4.2; 45 3.7; 49 3.3; 54 2.7; 60 2.2; 66 1.7; 72 1.6; 79 1.6; 87 1.3; 96 0.4; 106 -0.0; 116 -0.4; 128 -1.0; 141 -1.3; 155 -1.6; 170 -1.5; 187 -1.7; 206 -1.8; 227 -1.8; 249 -1.8; 274 -1.8; 302 -1.5; 332 -1.5; 365 -1.3; 402 -1.2; 442 -0.9; 486 -0.8; 535 -0.5; 588 1.0; 647 0.7; 712 0.7; 783 1.0; 861 0.5; 947 0.1; 1042 0.0; 1146 -0.4; 1261 -1.0; 1387 -1.9; 1526 -3.2; 1678 -4.3; 1846 -5.2; 2031 -5.5; 2234 -5.2; 2457 -3.9; 2703 -2.3; 2973 -1.2; 3270 -0.0; 3597 0.4; 3957 -0.5; 4353 -2.5; 4788 -1.9; 5267 -2.0; 5793 -3.6; 6373 -4.8; 7010 -4.5; 7711 -4.8; 8482 -5.5; 9330 -3.1; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.4; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.46 | 6.2 dB  |
| Peaking | 217 Hz   | 0.55 | -2.3 dB |
| Peaking | 728 Hz   | 1.53 | 1.8 dB  |
| Peaking | 1960 Hz  | 2.11 | -5.9 dB |
| Peaking | 7348 Hz  | 1.83 | -5.4 dB |
| Peaking | 2430 Hz  | 5.56 | -1.1 dB |
| Peaking | 3629 Hz  | 3.02 | 2.1 dB  |
| Peaking | 4385 Hz  | 6.43 | -2.0 dB |
| Peaking | 9255 Hz  | 1.57 | -1.1 dB |
| Peaking | 10256 Hz | 2.94 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q701%20Quincy%20Jones/AKG%20Q701%20Quincy%20Jones.png)