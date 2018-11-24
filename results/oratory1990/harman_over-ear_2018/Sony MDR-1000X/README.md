# Sony MDR-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -6.8; 23 -7.1; 25 -7.4; 28 -7.6; 31 -7.7; 34 -7.8; 37 -7.7; 41 -7.6; 45 -7.5; 49 -7.4; 54 -7.3; 60 -7.4; 66 -7.5; 72 -7.7; 79 -8.1; 87 -8.5; 96 -8.9; 106 -9.2; 116 -9.5; 128 -9.7; 141 -9.8; 155 -9.7; 170 -9.6; 187 -9.2; 206 -8.8; 227 -8.3; 249 -8.2; 274 -8.2; 302 -7.7; 332 -6.7; 365 -5.6; 402 -5.3; 442 -5.8; 486 -6.0; 535 -5.8; 588 -4.4; 647 -4.7; 712 -5.9; 783 -2.4; 861 -1.3; 947 -0.5; 1042 0.0; 1146 1.5; 1261 -0.4; 1387 -2.5; 1526 -5.3; 1678 -7.3; 1846 -8.2; 2031 -7.6; 2234 -5.7; 2457 -5.0; 2703 -4.9; 2973 -4.4; 3270 -4.4; 3597 -4.8; 3957 -7.7; 4353 -8.4; 4788 -6.6; 5267 -8.3; 5793 -12.7; 6373 -5.7; 7010 -2.3; 7711 -3.9; 8482 -4.0; 9330 -1.1; 10263 -0.0; 11289 -2.6; 12418 -6.2; 13660 -5.9; 15026 -0.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.14 | -6.9 dB |
| Peaking | 193 Hz   | 0.63 | -6.1 dB |
| Peaking | 543 Hz   | 2.09 | -3.1 dB |
| Peaking | 1885 Hz  | 3.07 | -7.5 dB |
| Peaking | 5146 Hz  | 1.1  | -8.8 dB |
| Peaking | 716 Hz   | 9.84 | -3.5 dB |
| Peaking | 1162 Hz  | 2.32 | 3.4 dB  |
| Peaking | 1518 Hz  | 4.25 | -2.7 dB |
| Peaking | 10072 Hz | 4.26 | 3.0 dB  |
| Peaking | 12904 Hz | 3.74 | -6.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-1000X/Sony%20MDR-1000X.png)