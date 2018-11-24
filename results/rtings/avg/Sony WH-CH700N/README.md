# Sony WH-CH700N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -6.6; 23 -6.8; 25 -7.0; 28 -7.2; 31 -7.3; 34 -7.1; 37 -6.9; 41 -6.6; 45 -6.1; 49 -5.7; 54 -5.1; 60 -4.6; 66 -4.4; 72 -4.3; 79 -4.3; 87 -4.4; 96 -4.5; 106 -4.9; 116 -5.2; 128 -5.4; 141 -5.5; 155 -5.3; 170 -5.0; 187 -4.7; 206 -4.5; 227 -4.5; 249 -4.4; 274 -4.1; 302 -3.8; 332 -3.4; 365 -2.8; 402 -2.2; 442 -1.9; 486 -1.4; 535 -0.8; 588 -0.6; 647 -0.5; 712 -0.7; 783 -0.9; 861 -0.8; 947 -0.4; 1042 0.3; 1146 0.6; 1261 0.1; 1387 -0.6; 1526 -2.0; 1678 -4.0; 1846 -6.2; 2031 -7.5; 2234 -6.1; 2457 -5.4; 2703 -5.9; 2973 -7.6; 3270 -9.3; 3597 -8.7; 3957 -4.7; 4353 0.1; 4788 -6.8; 5267 -13.8; 5793 -8.7; 6373 -4.7; 7010 -1.7; 7711 -1.1; 8482 -2.4; 9330 -3.8; 10263 -4.2; 11289 -4.3; 12418 -4.3; 13660 -1.0; 15026 -0.0; 16529 -5.7; 18182 -11.8; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.58 | -7.1 dB  |
| Peaking | 170 Hz   | 0.72 | -4.8 dB  |
| Peaking | 3866 Hz  | 0.6  | -7.5 dB  |
| Peaking | 18250 Hz | 2.32 | -12.0 dB |
| Peaking | 21627 Hz | 1.91 | -9.7 dB  |
| Peaking | 1225 Hz  | 2.05 | 2.9 dB   |
| Peaking | 1947 Hz  | 3.93 | -3.8 dB  |
| Peaking | 4422 Hz  | 6.84 | 11.0 dB  |
| Peaking | 5220 Hz  | 4.28 | -9.3 dB  |
| Peaking | 7211 Hz  | 4.71 | 4.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-CH700N/Sony%20WH-CH700N.png)