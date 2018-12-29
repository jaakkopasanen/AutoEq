# Focal Utopia

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.5; 37 5.3; 41 5.1; 45 4.9; 49 4.8; 54 4.5; 60 4.2; 66 3.9; 72 3.5; 79 3.2; 87 2.7; 96 2.3; 106 1.8; 116 1.5; 128 1.1; 141 0.9; 155 0.7; 170 0.5; 187 0.5; 206 0.4; 227 0.4; 249 0.5; 274 0.8; 302 1.0; 332 1.2; 365 1.4; 402 1.5; 442 1.6; 486 1.7; 535 1.8; 588 1.8; 647 1.7; 712 1.5; 783 1.1; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.4; 1261 -0.4; 1387 0.8; 1526 2.3; 1678 4.5; 1846 5.9; 2031 6.0; 2234 5.6; 2457 3.6; 2703 2.4; 2973 2.9; 3270 3.3; 3597 3.9; 3957 2.0; 4353 1.3; 4788 1.3; 5267 -0.1; 5793 -3.0; 6373 1.6; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.5; 18182 -5.2; 20000 -15.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.6  | 5.8 dB  |
| Peaking | 63 Hz   | 1.06 | 2.1 dB  |
| Peaking | 499 Hz  | 1.53 | 1.9 dB  |
| Peaking | 2000 Hz | 2.76 | 6.5 dB  |
| Peaking | 3479 Hz | 3.41 | 3.3 dB  |
| Peaking | 708 Hz  | 4.24 | 0.7 dB  |
| Peaking | 1201 Hz | 2.91 | -1.6 dB |
| Peaking | 1674 Hz | 6.47 | 1.3 dB  |
| Peaking | 5761 Hz | 9.6  | -4.3 dB |
| Peaking | 6726 Hz | 6.93 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Utopia/Focal%20Utopia.png)