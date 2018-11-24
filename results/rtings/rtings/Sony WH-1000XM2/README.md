# Sony WH-1000XM2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 21 -10.0; 23 -9.6; 25 -9.3; 28 -9.0; 31 -8.7; 34 -8.4; 37 -8.2; 41 -7.9; 45 -7.7; 49 -7.6; 54 -7.7; 60 -7.7; 66 -7.9; 72 -8.1; 79 -8.3; 87 -8.5; 96 -8.8; 106 -9.0; 116 -9.2; 128 -9.4; 141 -9.4; 155 -9.4; 170 -9.3; 187 -9.0; 206 -8.6; 227 -8.1; 249 -7.9; 274 -7.6; 302 -7.2; 332 -6.8; 365 -6.4; 402 -5.9; 442 -5.6; 486 -5.2; 535 -4.9; 588 -4.4; 647 -3.8; 712 -3.2; 783 -1.1; 861 0.3; 947 0.2; 1042 -0.6; 1146 -2.3; 1261 -4.6; 1387 -7.3; 1526 -9.0; 1678 -10.4; 1846 -11.8; 2031 -11.2; 2234 -8.9; 2457 -7.5; 2703 -7.5; 2973 -6.6; 3270 -6.3; 3597 -6.8; 3957 -7.7; 4353 -5.8; 4788 -3.1; 5267 -4.6; 5793 -5.4; 6373 -2.8; 7010 -3.9; 7711 -5.2; 8482 -6.4; 9330 -5.4; 10263 -2.8; 11289 -0.5; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 1.04 | -9.8 dB |
| Peaking | 39 Hz    | 0.16 | -6.5 dB |
| Peaking | 210 Hz   | 0.55 | -4.9 dB |
| Peaking | 1858 Hz  | 2.19 | -9.8 dB |
| Peaking | 4653 Hz  | 0.52 | -5.2 dB |
| Peaking | 898 Hz   | 0.88 | -3.8 dB |
| Peaking | 933 Hz   | 2.11 | 7.5 dB  |
| Peaking | 6869 Hz  | 1.91 | 3.5 dB  |
| Peaking | 8708 Hz  | 1.73 | -6.4 dB |
| Peaking | 11212 Hz | 1.33 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20WH-1000XM2/Sony%20WH-1000XM2.png)