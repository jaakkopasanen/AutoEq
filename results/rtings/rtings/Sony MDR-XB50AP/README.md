# Sony MDR-XB50AP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.5; 25 1.2; 28 0.8; 31 0.5; 34 0.3; 37 0.1; 41 -0.2; 45 -0.4; 49 -0.6; 54 -0.8; 60 -1.3; 66 -1.7; 72 -2.1; 79 -2.6; 87 -3.1; 96 -3.7; 106 -4.4; 116 -5.0; 128 -5.5; 141 -5.9; 155 -6.0; 170 -6.0; 187 -6.1; 206 -6.1; 227 -5.7; 249 -4.9; 274 -4.0; 302 -2.9; 332 -1.8; 365 -0.5; 402 0.9; 442 2.3; 486 3.5; 535 4.5; 588 4.8; 647 4.7; 712 4.1; 783 3.2; 861 2.1; 947 0.7; 1042 -0.5; 1146 -1.3; 1261 -1.7; 1387 -1.5; 1526 -0.7; 1678 0.4; 1846 1.0; 2031 1.6; 2234 3.3; 2457 5.5; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.5; 4353 4.1; 4788 2.6; 5267 1.2; 5793 3.4; 6373 2.8; 7010 2.4; 7711 0.3; 8482 0.0; 9330 -1.8; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB50AP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB50AP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.45 | 2.6 dB  |
| Peaking | 174 Hz  | 0.64 | -6.7 dB |
| Peaking | 558 Hz  | 1.69 | 6.8 dB  |
| Peaking | 2625 Hz | 3.89 | 4.3 dB  |
| Peaking | 3703 Hz | 1.81 | 5.6 dB  |
| Peaking | 567 Hz  | 3.43 | -2.3 dB |
| Peaking | 669 Hz  | 1.35 | 2.2 dB  |
| Peaking | 1232 Hz | 2.32 | -3.1 dB |
| Peaking | 6267 Hz | 5.73 | 2.5 dB  |
| Peaking | 9514 Hz | 7.46 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-XB50AP/Sony%20MDR-XB50AP.png)