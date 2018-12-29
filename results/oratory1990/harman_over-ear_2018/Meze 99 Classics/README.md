# Meze 99 Classics

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.4; 28 -8.7; 31 -8.9; 34 -9.0; 37 -9.2; 41 -9.3; 45 -9.5; 49 -9.5; 54 -9.6; 60 -9.8; 66 -9.9; 72 -9.9; 79 -9.8; 87 -9.6; 96 -9.5; 106 -9.3; 116 -9.6; 128 -10.2; 141 -9.8; 155 -10.8; 170 -11.3; 187 -11.1; 206 -10.9; 227 -10.1; 249 -9.3; 274 -7.7; 302 -5.3; 332 -2.7; 365 -1.0; 402 -0.8; 442 -1.5; 486 -2.3; 535 -2.9; 588 -3.1; 647 -3.1; 712 -2.9; 783 -2.4; 861 -1.7; 947 -0.6; 1042 -0.1; 1146 -0.9; 1261 -1.2; 1387 -1.8; 1526 -2.6; 1678 -3.5; 1846 -3.6; 2031 -2.6; 2234 -1.4; 2457 -0.9; 2703 -0.6; 2973 0.4; 3270 2.5; 3597 5.6; 3957 5.5; 4353 -2.5; 4788 -7.1; 5267 -6.8; 5793 -5.8; 6373 -6.3; 7010 -5.9; 7711 -5.7; 8482 -3.0; 9330 0.0; 10263 0.0; 11289 -3.0; 12418 -10.4; 13660 -9.5; 15026 -4.1; 16529 -3.2; 18182 -5.1; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Classics GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Classics ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.46 | -5.1 dB  |
| Peaking | 87 Hz    | 0.36 | -8.0 dB  |
| Peaking | 200 Hz   | 1.76 | -5.9 dB  |
| Peaking | 6050 Hz  | 2.36 | -7.1 dB  |
| Peaking | 13213 Hz | 2.88 | -11.5 dB |
| Peaking | 374 Hz   | 5.78 | 3.4 dB   |
| Peaking | 1782 Hz  | 2.05 | -3.5 dB  |
| Peaking | 3808 Hz  | 3.74 | 9.2 dB   |
| Peaking | 4707 Hz  | 4.8  | -6.7 dB  |
| Peaking | 10254 Hz | 6.06 | 3.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%2099%20Classics/Meze%2099%20Classics.png)