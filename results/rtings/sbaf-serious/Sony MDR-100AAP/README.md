# Sony MDR-100AAP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 -1.5; 23 -2.1; 25 -2.5; 28 -3.2; 31 -3.8; 34 -4.3; 37 -4.6; 41 -4.9; 45 -5.1; 49 -5.2; 54 -5.2; 60 -5.2; 66 -5.2; 72 -5.0; 79 -5.0; 87 -5.2; 96 -5.5; 106 -5.8; 116 -6.0; 128 -6.0; 141 -5.7; 155 -5.5; 170 -5.3; 187 -4.8; 206 -4.1; 227 -2.9; 249 -2.7; 274 -3.7; 302 -2.5; 332 -1.2; 365 -0.2; 402 0.3; 442 0.5; 486 0.6; 535 0.5; 588 0.5; 647 0.5; 712 0.4; 783 0.2; 861 -0.0; 947 -0.0; 1042 0.1; 1146 0.3; 1261 0.3; 1387 -0.1; 1526 -0.5; 1678 -0.6; 1846 0.0; 2031 0.5; 2234 1.4; 2457 2.3; 2703 3.3; 2973 4.3; 3270 4.3; 3597 4.2; 3957 2.9; 4353 1.7; 4788 3.5; 5267 0.6; 5793 3.5; 6373 4.1; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -0.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-100AAP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-100AAP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.71 | -4.8 dB |
| Peaking | 120 Hz  | 1.3  | -3.8 dB |
| Peaking | 194 Hz  | 1.56 | -2.7 dB |
| Peaking | 3254 Hz | 2.04 | 4.7 dB  |
| Peaking | 6289 Hz | 5.07 | 4.3 dB  |
| Peaking | 284 Hz  | 6.05 | -2.2 dB |
| Peaking | 446 Hz  | 1.25 | 1.2 dB  |
| Peaking | 1655 Hz | 3.64 | -1.3 dB |
| Peaking | 3713 Hz | 0.49 | 0.2 dB  |
| Peaking | 8791 Hz | 6.4  | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-100AAP/Sony%20MDR-100AAP.png)