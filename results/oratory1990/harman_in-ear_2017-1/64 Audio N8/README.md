# 64 Audio N8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 5.2; 66 4.3; 72 3.8; 79 3.0; 87 2.3; 96 2.2; 106 1.2; 116 0.8; 128 0.0; 141 -0.5; 155 -1.0; 170 -1.6; 187 -2.3; 206 -2.7; 227 -3.0; 249 -3.2; 274 -3.2; 302 -3.0; 332 -2.9; 365 -2.6; 402 -2.5; 442 -2.4; 486 -2.1; 535 -1.9; 588 -1.6; 647 -1.2; 712 -0.8; 783 -0.4; 861 0.0; 947 0.1; 1042 -0.2; 1146 -0.8; 1261 -1.6; 1387 -2.0; 1526 -2.1; 1678 -1.9; 1846 -1.6; 2031 -1.0; 2234 0.1; 2457 1.5; 2703 2.9; 2973 4.0; 3270 4.6; 3597 4.5; 3957 3.7; 4353 2.8; 4788 1.9; 5267 2.4; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -9.9; 15026 -19.8; 16529 -19.0; 18182 -11.9; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.29 | 7.3 dB   |
| Peaking | 194 Hz   | 0.42 | -5.3 dB  |
| Peaking | 5885 Hz  | 0.76 | 6.7 dB   |
| Peaking | 12225 Hz | 2.27 | 11.1 dB  |
| Peaking | 15467 Hz | 1.09 | -24.9 dB |
| Peaking | 934 Hz   | 1.46 | 2.5 dB   |
| Peaking | 1659 Hz  | 0.86 | -3.9 dB  |
| Peaking | 3250 Hz  | 1.33 | 4.8 dB   |
| Peaking | 5145 Hz  | 1.76 | -5.1 dB  |
| Peaking | 5950 Hz  | 4.34 | 5.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/64%20Audio%20N8/64%20Audio%20N8.png)