# Focal Utopia

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.6; 106 4.7; 116 3.9; 128 3.0; 141 2.3; 155 1.7; 170 1.2; 187 0.8; 206 0.5; 227 0.4; 249 0.5; 274 0.8; 302 1.0; 332 1.2; 365 1.4; 402 1.5; 442 1.6; 486 1.7; 535 1.8; 588 1.8; 647 1.7; 712 1.5; 783 1.1; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.4; 1261 -0.4; 1387 0.8; 1526 2.3; 1678 4.5; 1846 5.9; 2031 6.0; 2234 5.6; 2457 3.6; 2703 2.4; 2973 2.9; 3270 3.3; 3597 3.9; 3957 2.0; 4353 1.3; 4788 1.3; 5267 -0.1; 5793 -3.0; 6373 1.6; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.5; 18182 -5.2; 20000 -15.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  0.43 | 6.8 dB  |
| Peaking | 546 Hz  |  2.19 | 1.7 dB  |
| Peaking | 1978 Hz |  2.96 | 6.2 dB  |
| Peaking | 3491 Hz |  1.8  | 2.8 dB  |
| Peaking | 5675 Hz | 10.4  | -4.0 dB |
| Peaking | 21 Hz   |  2.96 | 1.1 dB  |
| Peaking | 92 Hz   |  3.67 | 1.5 dB  |
| Peaking | 191 Hz  |  2.29 | -1.3 dB |
| Peaking | 1194 Hz |  5.13 | -1.6 dB |
| Peaking | 6782 Hz |  9.8  | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Utopia/Focal%20Utopia.png)