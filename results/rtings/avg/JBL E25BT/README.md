# JBL E25BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.5dB
GraphicEQ: 21 -3.1; 23 -3.4; 25 -3.7; 28 -4.0; 31 -4.3; 34 -4.5; 37 -4.7; 41 -4.9; 45 -5.0; 49 -5.1; 54 -5.3; 60 -5.8; 66 -6.2; 72 -6.5; 79 -6.9; 87 -7.3; 96 -7.7; 106 -8.2; 116 -8.5; 128 -8.9; 141 -9.2; 155 -9.3; 170 -9.2; 187 -9.1; 206 -8.9; 227 -8.6; 249 -8.0; 274 -7.5; 302 -6.8; 332 -6.3; 365 -5.8; 402 -5.2; 442 -4.4; 486 -3.6; 535 -2.8; 588 -1.9; 647 -0.9; 712 0.1; 783 1.0; 861 1.4; 947 0.7; 1042 -0.5; 1146 -1.4; 1261 -1.8; 1387 -2.0; 1526 -1.7; 1678 -1.4; 1846 -1.5; 2031 -1.6; 2234 -1.1; 2457 -0.7; 2703 -1.2; 2973 -2.7; 3270 -4.2; 3597 -4.8; 3957 -4.8; 4353 -5.0; 4788 -5.1; 5267 -5.9; 5793 -7.9; 6373 -10.4; 7010 -7.8; 7711 -3.2; 8482 -2.2; 9330 -5.8; 10263 -6.8; 11289 -2.4; 12418 0.0; 13660 -1.0; 15026 -7.3; 16529 -11.4; 18182 -11.0; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E25BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-15**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E25BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 69 Hz    | 0.31 | -4.9 dB  |
| Peaking | 200 Hz   | 0.69 | -6.3 dB  |
| Peaking | 5927 Hz  | 1.07 | -7.9 dB  |
| Peaking | 16614 Hz | 2.78 | -8.7 dB  |
| Peaking | 19255 Hz | 1.43 | -10.3 dB |
| Peaking | 816 Hz   | 3.25 | 3.4 dB   |
| Peaking | 5715 Hz  | 0.04 | -0.5 dB  |
| Peaking | 8186 Hz  | 6.24 | 4.8 dB   |
| Peaking | 10055 Hz | 4.3  | -4.7 dB  |
| Peaking | 12504 Hz | 3.23 | 4.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E25BT/JBL%20E25BT.png)