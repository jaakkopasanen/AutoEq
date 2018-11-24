# Beats Solo II 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -4.9; 23 -5.1; 25 -5.2; 28 -5.4; 31 -5.5; 34 -5.6; 37 -5.7; 41 -5.7; 45 -5.8; 49 -5.8; 54 -5.9; 60 -6.1; 66 -6.3; 72 -6.5; 79 -6.8; 87 -7.1; 96 -7.3; 106 -7.5; 116 -7.6; 128 -7.7; 141 -7.9; 155 -8.2; 170 -8.0; 187 -8.0; 206 -8.0; 227 -7.9; 249 -7.6; 274 -7.2; 302 -6.4; 332 -5.6; 365 -5.3; 402 -4.8; 442 -4.1; 486 -3.9; 535 -3.6; 588 -2.9; 647 -1.5; 712 -0.8; 783 -0.6; 861 -1.0; 947 -0.4; 1042 -0.3; 1146 -0.8; 1261 -1.0; 1387 -1.2; 1526 -1.2; 1678 -1.1; 1846 -0.5; 2031 0.1; 2234 0.6; 2457 1.3; 2703 1.8; 2973 1.4; 3270 0.6; 3597 0.2; 3957 0.8; 4353 0.4; 4788 -2.0; 5267 1.1; 5793 2.6; 6373 1.8; 7010 0.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo II 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo II 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.38 | -4.7 dB |
| Peaking | 110 Hz  | 0.68 | -3.4 dB |
| Peaking | 241 Hz  | 0.65 | -5.9 dB |
| Peaking | 2723 Hz | 4.01 | 2.0 dB  |
| Peaking | 5971 Hz | 5.93 | 2.8 dB  |
| Peaking | 565 Hz  | 2.6  | -2.0 dB |
| Peaking | 657 Hz  | 1.64 | 1.8 dB  |
| Peaking | 1502 Hz | 3.29 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo%20II%202014/Beats%20Solo%20II%202014.png)