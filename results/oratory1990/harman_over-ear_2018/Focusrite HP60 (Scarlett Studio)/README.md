# Focusrite HP60 (Scarlett Studio)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.9; 79 5.5; 87 5.2; 96 5.2; 106 4.5; 116 3.3; 128 2.5; 141 1.8; 155 1.4; 170 1.1; 187 0.7; 206 0.5; 227 0.4; 249 0.7; 274 1.2; 302 1.8; 332 2.3; 365 2.3; 402 1.4; 442 0.2; 486 -0.6; 535 -0.8; 588 -0.3; 647 1.0; 712 0.7; 783 0.2; 861 0.2; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.0; 1387 0.7; 1526 1.3; 1678 2.0; 1846 2.6; 2031 2.7; 2234 2.6; 2457 2.8; 2703 3.2; 2973 3.2; 3270 4.6; 3597 5.9; 3957 6.0; 4353 6.0; 4788 1.1; 5267 -6.3; 5793 -6.0; 6373 -0.1; 7010 1.5; 7711 -0.0; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.4; 16529 -4.7; 18182 -4.4; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focusrite HP60 (Scarlett Studio) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focusrite HP60 (Scarlett Studio) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 42 Hz   | 0.44 | 6.7 dB   |
| Peaking | 347 Hz  | 5.91 | 2.2 dB   |
| Peaking | 4428 Hz | 1.28 | 18.4 dB  |
| Peaking | 5335 Hz | 1.76 | -21.1 dB |
| Peaking | 6746 Hz | 5.9  | 6.0 dB   |
| Peaking | 17 Hz   | 2.87 | 1.1 dB   |
| Peaking | 96 Hz   | 5.38 | 1.4 dB   |
| Peaking | 516 Hz  | 6.21 | -1.5 dB  |
| Peaking | 1175 Hz | 3.74 | -1.2 dB  |
| Peaking | 1861 Hz | 4.06 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focusrite%20HP60%20(Scarlett%20Studio)/Focusrite%20HP60%20(Scarlett%20Studio).png)