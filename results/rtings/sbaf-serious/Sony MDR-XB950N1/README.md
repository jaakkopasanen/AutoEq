# Sony MDR-XB950N1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.0; 23 -7.2; 25 -7.4; 28 -7.6; 31 -7.7; 34 -7.8; 37 -7.7; 41 -7.7; 45 -7.6; 49 -7.5; 54 -7.3; 60 -7.2; 66 -7.1; 72 -7.0; 79 -7.1; 87 -7.4; 96 -7.7; 106 -7.8; 116 -7.7; 128 -7.3; 141 -6.7; 155 -6.1; 170 -5.3; 187 -4.6; 206 -3.5; 227 -2.2; 249 -0.8; 274 0.6; 302 1.9; 332 2.5; 365 2.6; 402 2.3; 442 1.9; 486 1.5; 535 1.2; 588 1.0; 647 0.9; 712 0.8; 783 0.5; 861 0.2; 947 0.0; 1042 0.0; 1146 -0.0; 1261 -0.0; 1387 0.0; 1526 -0.1; 1678 0.0; 1846 0.7; 2031 2.1; 2234 3.8; 2457 5.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950N1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950N1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.56 | -6.5 dB |
| Peaking | 130 Hz  | 0.5  | -7.1 dB |
| Peaking | 331 Hz  | 1.16 | 6.0 dB  |
| Peaking | 3182 Hz | 1.47 | 6.5 dB  |
| Peaking | 5677 Hz | 2.79 | 5.1 dB  |
| Peaking | 1694 Hz | 1.98 | -1.6 dB |
| Peaking | 2455 Hz | 3.4  | 2.4 dB  |
| Peaking | 3147 Hz | 3.28 | -1.3 dB |
| Peaking | 4236 Hz | 5.6  | 1.5 dB  |
| Peaking | 8359 Hz | 3.62 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-XB950N1/Sony%20MDR-XB950N1.png)