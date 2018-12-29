# Focusrite HP60 (Scarlett Studio)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 4.9; 49 4.0; 54 3.1; 60 2.3; 66 1.7; 72 1.4; 79 1.3; 87 1.4; 96 1.9; 106 1.7; 116 1.0; 128 0.6; 141 0.4; 155 0.4; 170 0.4; 187 0.4; 206 0.4; 227 0.4; 249 0.7; 274 1.2; 302 1.8; 332 2.3; 365 2.3; 402 1.4; 442 0.2; 486 -0.6; 535 -0.8; 588 -0.3; 647 1.0; 712 0.7; 783 0.2; 861 0.2; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.0; 1387 0.7; 1526 1.3; 1678 2.0; 1846 2.6; 2031 2.7; 2234 2.6; 2457 2.8; 2703 3.2; 2973 3.2; 3270 4.6; 3597 5.9; 3957 6.0; 4353 6.0; 4788 1.1; 5267 -6.3; 5793 -6.0; 6373 -0.1; 7010 1.5; 7711 -0.0; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.4; 16529 -4.7; 18182 -4.4; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focusrite HP60 (Scarlett Studio) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focusrite HP60 (Scarlett Studio) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.72 | 6.5 dB   |
| Peaking | 337 Hz  | 3.88 | 2.5 dB   |
| Peaking | 4430 Hz | 1.27 | 18.7 dB  |
| Peaking | 5334 Hz | 1.73 | -21.4 dB |
| Peaking | 6749 Hz | 5.85 | 6.0 dB   |
| Peaking | 527 Hz  | 3.3  | -2.8 dB  |
| Peaking | 569 Hz  | 1.52 | 1.6 dB   |
| Peaking | 1147 Hz | 1.98 | -1.2 dB  |
| Peaking | 1822 Hz | 3.6  | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focusrite%20HP60%20(Scarlett%20Studio)/Focusrite%20HP60%20(Scarlett%20Studio).png)