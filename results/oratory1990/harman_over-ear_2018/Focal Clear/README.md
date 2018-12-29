# Focal Clear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.6; 28 5.3; 31 5.1; 34 4.9; 37 4.7; 41 4.5; 45 4.4; 49 4.2; 54 3.9; 60 3.7; 66 3.4; 72 3.1; 79 2.8; 87 2.4; 96 2.1; 106 1.7; 116 1.4; 128 1.1; 141 0.9; 155 0.8; 170 0.7; 187 0.7; 206 0.7; 227 0.8; 249 0.9; 274 1.1; 302 1.3; 332 1.5; 365 1.8; 402 1.9; 442 1.9; 486 2.0; 535 2.0; 588 2.0; 647 1.9; 712 1.6; 783 1.3; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.4; 1387 -1.4; 1526 -0.8; 1678 0.2; 1846 1.2; 2031 2.0; 2234 2.5; 2457 2.2; 2703 1.7; 2973 1.1; 3270 1.5; 3597 1.8; 3957 4.9; 4353 6.0; 4788 5.6; 5267 5.0; 5793 1.6; 6373 4.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.9; 13660 0.0; 15026 0.0; 16529 -0.8; 18182 -3.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Clear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  0.56 | 5.6 dB  |
| Peaking | 59 Hz    |  0.82 | 2.1 dB  |
| Peaking | 475 Hz   |  1.33 | 2.2 dB  |
| Peaking | 2251 Hz  |  5.05 | 2.3 dB  |
| Peaking | 4696 Hz  |  2.09 | 6.1 dB  |
| Peaking | 715 Hz   |  3.64 | 0.8 dB  |
| Peaking | 1298 Hz  |  3.49 | -2.1 dB |
| Peaking | 3520 Hz  |  8.86 | -0.8 dB |
| Peaking | 6544 Hz  | 13.18 | 3.6 dB  |
| Peaking | 19753 Hz |  1.54 | -6.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Clear/Focal%20Clear.png)