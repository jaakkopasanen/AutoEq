# Sony WH-1000XM2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 21 -6.4; 23 -6.7; 25 -6.9; 28 -7.2; 31 -7.4; 34 -7.6; 37 -7.7; 41 -7.8; 45 -7.8; 49 -7.8; 54 -7.7; 60 -7.6; 66 -7.6; 72 -7.6; 79 -7.7; 87 -7.9; 96 -8.2; 106 -8.5; 116 -8.8; 128 -9.0; 141 -9.1; 155 -9.2; 170 -9.2; 187 -9.1; 206 -9.0; 227 -8.7; 249 -8.2; 274 -7.7; 302 -7.1; 332 -6.4; 365 -5.7; 402 -5.1; 442 -4.6; 486 -4.2; 535 -3.8; 588 -3.5; 647 -3.0; 712 -2.5; 783 0.5; 861 0.3; 947 0.1; 1042 -0.5; 1146 -2.7; 1261 -5.5; 1387 -7.0; 1526 -8.1; 1678 -7.9; 1846 -7.0; 2031 -6.7; 2234 -6.5; 2457 -6.5; 2703 -7.3; 2973 -6.7; 3270 -4.4; 3597 -4.3; 3957 -6.5; 4353 -6.6; 4788 -5.3; 5267 -7.8; 5793 -10.5; 6373 -5.6; 7010 -4.7; 7711 -6.7; 8482 -4.3; 9330 -0.1; 10263 -0.2; 11289 -5.1; 12418 -10.5; 13660 -9.1; 15026 -3.9; 16529 -3.2; 18182 -5.7; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-11**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.22 | -7.2 dB  |
| Peaking | 217 Hz   | 0.74 | -5.7 dB  |
| Peaking | 1994 Hz  | 1.1  | -7.4 dB  |
| Peaking | 5619 Hz  | 1.77 | -7.7 dB  |
| Peaking | 13093 Hz | 2.59 | -10.7 dB |
| Peaking | 960 Hz   | 1.8  | 8.5 dB   |
| Peaking | 1204 Hz  | 0.78 | -5.9 dB  |
| Peaking | 2015 Hz  | 2.91 | 4.0 dB   |
| Peaking | 10028 Hz | 5.96 | 4.3 dB   |
| Peaking | 19728 Hz | 1.65 | -8.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20WH-1000XM2/Sony%20WH-1000XM2.png)