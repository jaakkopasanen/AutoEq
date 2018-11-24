# Apple In-Ear 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.2; 25 1.2; 28 1.2; 31 1.2; 34 1.2; 37 1.1; 41 1.0; 45 0.9; 49 0.7; 54 0.6; 60 0.4; 66 0.1; 72 -0.2; 79 -0.5; 87 -0.9; 96 -1.3; 106 -1.5; 116 -1.8; 128 -2.1; 141 -2.4; 155 -2.5; 170 -2.6; 187 -2.8; 206 -2.7; 227 -2.8; 249 -2.7; 274 -2.7; 302 -2.5; 332 -2.4; 365 -2.2; 402 -2.0; 442 -1.7; 486 -1.6; 535 -1.2; 588 -0.4; 647 -0.1; 712 -0.1; 783 0.2; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.5; 1526 -0.8; 1678 -0.8; 1846 -0.5; 2031 -0.0; 2234 0.2; 2457 0.5; 2703 0.3; 2973 1.4; 3270 4.3; 3597 6.0; 3957 5.5; 4353 3.0; 4788 3.0; 5267 5.1; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple In-Ear 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple In-Ear 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.57 | 1.5 dB  |
| Peaking | 202 Hz  | 0.58 | -3.0 dB |
| Peaking | 3639 Hz | 4.24 | 6.0 dB  |
| Peaking | 5998 Hz | 2.51 | 6.8 dB  |
| Peaking | 7750 Hz | 2.04 | -1.8 dB |
| Peaking | 787 Hz  | 2.71 | 0.8 dB  |
| Peaking | 1622 Hz | 3.28 | -1.0 dB |
| Peaking | 2797 Hz | 8.02 | -0.7 dB |
| Peaking | 5294 Hz | 4.53 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20In-Ear%202013/Apple%20In-Ear%202013.png)