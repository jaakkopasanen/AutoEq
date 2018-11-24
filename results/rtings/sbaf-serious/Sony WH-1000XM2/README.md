# Sony WH-1000XM2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.5dB
GraphicEQ: 21 -9.6; 23 -9.3; 25 -9.1; 28 -8.8; 31 -8.6; 34 -8.5; 37 -8.3; 41 -8.1; 45 -8.0; 49 -8.0; 54 -8.0; 60 -8.0; 66 -8.1; 72 -8.1; 79 -8.1; 87 -8.2; 96 -8.3; 106 -8.5; 116 -8.7; 128 -8.8; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.4; 206 -8.1; 227 -7.6; 249 -7.4; 274 -6.9; 302 -6.4; 332 -5.9; 365 -5.4; 402 -4.9; 442 -4.5; 486 -4.0; 535 -3.7; 588 -3.3; 647 -2.8; 712 -2.3; 783 -0.6; 861 0.4; 947 0.2; 1042 -0.5; 1146 -2.1; 1261 -4.3; 1387 -7.4; 1526 -9.4; 1678 -10.8; 1846 -11.8; 2031 -10.8; 2234 -8.4; 2457 -7.1; 2703 -6.9; 2973 -5.5; 3270 -4.4; 3597 -4.7; 3957 -6.5; 4353 -5.8; 4788 -3.3; 5267 -4.1; 5793 -3.9; 6373 -0.3; 7010 -1.4; 7711 -4.1; 8482 -6.1; 9330 -3.9; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 1.25 | -9.4 dB  |
| Peaking | 41 Hz    | 0.21 | -7.2 dB  |
| Peaking | 210 Hz   | 0.65 | -4.7 dB  |
| Peaking | 1821 Hz  | 2.24 | -10.5 dB |
| Peaking | 4156 Hz  | 0.62 | -4.2 dB  |
| Peaking | 919 Hz   | 0.9  | -3.7 dB  |
| Peaking | 926 Hz   | 1.98 | 6.9 dB   |
| Peaking | 6598 Hz  | 6.04 | 4.0 dB   |
| Peaking | 8699 Hz  | 3.13 | -6.7 dB  |
| Peaking | 10027 Hz | 1.78 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WH-1000XM2/Sony%20WH-1000XM2.png)