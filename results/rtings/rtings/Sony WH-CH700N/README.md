# Sony WH-CH700N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -6.6; 23 -6.8; 25 -7.0; 28 -7.2; 31 -7.3; 34 -7.1; 37 -6.9; 41 -6.6; 45 -6.1; 49 -5.7; 54 -5.1; 60 -4.6; 66 -4.4; 72 -4.3; 79 -4.3; 87 -4.4; 96 -4.5; 106 -4.9; 116 -5.2; 128 -5.4; 141 -5.5; 155 -5.3; 170 -5.0; 187 -4.7; 206 -4.5; 227 -4.5; 249 -4.4; 274 -4.1; 302 -3.8; 332 -3.4; 365 -2.8; 402 -2.2; 442 -1.9; 486 -1.4; 535 -0.8; 588 -0.6; 647 -0.5; 712 -0.7; 783 -0.9; 861 -0.8; 947 -0.4; 1042 0.3; 1146 0.6; 1261 0.1; 1387 -0.6; 1526 -2.0; 1678 -4.0; 1846 -6.2; 2031 -7.5; 2234 -6.1; 2457 -5.4; 2703 -5.7; 2973 -7.2; 3270 -8.5; 3597 -7.7; 3957 -3.5; 4353 1.4; 4788 -5.0; 5267 -11.3; 5793 -6.3; 6373 -3.5; 7010 -1.1; 7711 -0.7; 8482 -3.3; 9330 -6.5; 10263 -6.4; 11289 -3.4; 12418 -1.0; 13660 0.0; 15026 0.0; 16529 -2.6; 18182 -7.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-15**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.59 | -7.1 dB |
| Peaking | 170 Hz   | 0.7  | -4.8 dB |
| Peaking | 3095 Hz  | 0.83 | -7.0 dB |
| Peaking | 9883 Hz  | 3.88 | -6.5 dB |
| Peaking | 18066 Hz | 3.18 | -8.3 dB |
| Peaking | 1217 Hz  | 2.14 | 2.6 dB  |
| Peaking | 1934 Hz  | 5.03 | -3.7 dB |
| Peaking | 4402 Hz  | 6.84 | 9.6 dB  |
| Peaking | 5212 Hz  | 4.9  | -9.1 dB |
| Peaking | 7345 Hz  | 5.84 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20WH-CH700N/Sony%20WH-CH700N.png)