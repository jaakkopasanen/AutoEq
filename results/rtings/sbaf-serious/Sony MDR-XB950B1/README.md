# Sony MDR-XB950B1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.1; 23 -6.4; 25 -6.6; 28 -6.9; 31 -7.0; 34 -7.1; 37 -7.1; 41 -7.1; 45 -7.1; 49 -7.1; 54 -7.1; 60 -7.2; 66 -7.3; 72 -7.4; 79 -7.5; 87 -7.7; 96 -7.9; 106 -8.1; 116 -8.2; 128 -8.2; 141 -7.8; 155 -7.2; 170 -6.4; 187 -6.3; 206 -5.5; 227 -4.1; 249 -2.5; 274 -0.5; 302 2.0; 332 4.7; 365 6.0; 402 4.9; 442 2.6; 486 1.2; 535 0.4; 588 -0.0; 647 -0.1; 712 -0.1; 783 -0.2; 861 -0.3; 947 -0.2; 1042 0.4; 1146 1.3; 1261 1.4; 1387 1.6; 1526 1.5; 1678 1.7; 1846 2.5; 2031 3.2; 2234 3.9; 2457 5.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 3.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950B1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950B1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.57 | -7.4 dB |
| Peaking | 114 Hz  | 1.63 | -6.3 dB |
| Peaking | 184 Hz  | 3.72 | -4.2 dB |
| Peaking | 3091 Hz | 1.07 | 6.1 dB  |
| Peaking | 5685 Hz | 3.13 | 4.7 dB  |
| Peaking | 40 Hz   | 3.98 | 0.4 dB  |
| Peaking | 239 Hz  | 2.27 | -2.4 dB |
| Peaking | 362 Hz  | 2.37 | 7.8 dB  |
| Peaking | 590 Hz  | 1.15 | -1.2 dB |
| Peaking | 8431 Hz | 3.69 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-XB950B1/Sony%20MDR-XB950B1.png)