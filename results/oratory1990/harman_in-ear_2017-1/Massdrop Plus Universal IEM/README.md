# Massdrop Plus Universal IEM

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.4; 60 4.7; 66 4.0; 72 3.2; 79 2.4; 87 1.6; 96 0.7; 106 -0.0; 116 -0.8; 128 -1.5; 141 -2.1; 155 -2.6; 170 -3.1; 187 -3.4; 206 -3.6; 227 -3.7; 249 -3.6; 274 -3.3; 302 -2.9; 332 -2.4; 365 -1.9; 402 -1.5; 442 -1.3; 486 -1.0; 535 -0.6; 588 -0.3; 647 0.1; 712 0.4; 783 0.6; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.5; 1387 -1.8; 1526 -2.2; 1678 -2.4; 1846 -2.6; 2031 -2.5; 2234 -1.9; 2457 -1.0; 2703 -0.1; 2973 0.7; 3270 1.0; 3597 1.0; 3957 0.7; 4353 0.4; 4788 0.7; 5267 1.9; 5793 3.0; 6373 3.2; 7010 1.1; 7711 -1.0; 8482 -1.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -6.6; 15026 -17.1; 16529 -14.7; 18182 -4.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus Universal IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus Universal IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.38 | 7.0 dB   |
| Peaking | 198 Hz   | 0.53 | -6.0 dB  |
| Peaking | 1796 Hz  | 1.03 | -5.2 dB  |
| Peaking | 4821 Hz  | 0.06 | 2.8 dB   |
| Peaking | 15685 Hz | 2.21 | -22.4 dB |
| Peaking | 4584 Hz  | 3.94 | -1.9 dB  |
| Peaking | 6325 Hz  | 2.11 | 2.9 dB   |
| Peaking | 7810 Hz  | 3.14 | -3.9 dB  |
| Peaking | 12870 Hz | 3.34 | 5.1 dB   |
| Peaking | 14404 Hz | 5.24 | -5.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Massdrop%20Plus%20Universal%20IEM/Massdrop%20Plus%20Universal%20IEM.png)