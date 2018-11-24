# Beyerdynamic DT 990 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.3; 28 0.6; 31 0.0; 34 -0.5; 37 -0.9; 41 -1.3; 45 -1.6; 49 -1.9; 54 -2.2; 60 -2.5; 66 -2.9; 72 -3.2; 79 -3.5; 87 -3.8; 96 -4.1; 106 -4.4; 116 -4.6; 128 -4.7; 141 -4.8; 155 -4.7; 170 -4.6; 187 -4.5; 206 -4.1; 227 -3.7; 249 -3.3; 274 -2.9; 302 -2.5; 332 -2.2; 365 -1.7; 402 -1.5; 442 -1.5; 486 -1.8; 535 -1.5; 588 -1.0; 647 -0.5; 712 -0.1; 783 0.0; 861 0.1; 947 0.1; 1042 0.0; 1146 0.1; 1261 0.0; 1387 -0.1; 1526 -0.3; 1678 -1.0; 1846 -1.8; 2031 -2.2; 2234 -1.8; 2457 -1.3; 2703 -1.6; 2973 -1.7; 3270 -1.3; 3597 0.4; 3957 2.8; 4353 -0.9; 4788 -1.7; 5267 0.4; 5793 0.2; 6373 -4.1; 7010 -3.0; 7711 -2.5; 8482 -7.4; 9330 -10.3; 10263 -6.5; 11289 -2.6; 12418 -3.3; 13660 -5.4; 15026 -4.9; 16529 -2.7; 18182 -3.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  0.94 | 3.7 dB  |
| Peaking | 44 Hz    |  0.56 | -1.1 dB |
| Peaking | 144 Hz   |  0.57 | -4.6 dB |
| Peaking | 9214 Hz  |  4.23 | -8.9 dB |
| Peaking | 21082 Hz |  0.2  | -4.7 dB |
| Peaking | 2018 Hz  |  4.46 | -2.1 dB |
| Peaking | 2977 Hz  |  2.97 | -1.5 dB |
| Peaking | 3916 Hz  |  8.59 | 3.9 dB  |
| Peaking | 6613 Hz  | 12.11 | -3.4 dB |
| Peaking | 14024 Hz |  5.62 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beyerdynamic%20DT%20990%20PRO/Beyerdynamic%20DT%20990%20PRO.png)