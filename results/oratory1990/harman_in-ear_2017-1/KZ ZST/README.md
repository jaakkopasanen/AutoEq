# KZ ZST

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.8; 31 5.6; 34 5.4; 37 5.2; 41 4.9; 45 4.5; 49 4.1; 54 3.7; 60 3.1; 66 2.5; 72 1.9; 79 1.3; 87 0.7; 96 0.1; 106 -0.5; 116 -1.0; 128 -1.3; 141 -1.6; 155 -2.1; 170 -3.1; 187 -3.2; 206 -3.2; 227 -3.2; 249 -2.9; 274 -2.6; 302 -2.1; 332 -1.6; 365 -1.1; 402 -0.8; 442 -0.5; 486 -0.1; 535 0.2; 588 0.4; 647 0.6; 712 0.8; 783 0.8; 861 0.4; 947 0.3; 1042 -0.3; 1146 -0.8; 1261 -1.3; 1387 -1.6; 1526 -2.0; 1678 -2.8; 1846 -3.5; 2031 -3.4; 2234 -1.9; 2457 -0.3; 2703 1.4; 2973 1.8; 3270 1.1; 3597 1.7; 3957 5.5; 4353 6.0; 4788 5.3; 5267 0.2; 5793 0.5; 6373 -0.9; 7010 -1.6; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 -6.2; 11289 -9.5; 12418 -10.5; 13660 -15.3; 15026 -19.3; 16529 -15.3; 18182 -7.8; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.55 | 6.1 dB   |
| Peaking | 193 Hz   | 1.1  | -3.8 dB  |
| Peaking | 1855 Hz  | 2.86 | -4.0 dB  |
| Peaking | 4326 Hz  | 2.43 | 7.1 dB   |
| Peaking | 15122 Hz | 1.44 | -20.7 dB |
| Peaking | 709 Hz   | 2.59 | 1.3 dB   |
| Peaking | 2794 Hz  | 7.2  | 2.0 dB   |
| Peaking | 8378 Hz  | 0.65 | -2.2 dB  |
| Peaking | 9102 Hz  | 2    | 7.3 dB   |
| Peaking | 10752 Hz | 3.58 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZST/KZ%20ZST.png)