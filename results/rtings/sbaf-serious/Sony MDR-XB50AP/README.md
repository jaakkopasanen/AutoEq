# Sony MDR-XB50AP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.4; 28 1.0; 31 0.6; 34 0.3; 37 -0.0; 41 -0.4; 45 -0.7; 49 -0.9; 54 -1.2; 60 -1.6; 66 -1.9; 72 -2.1; 79 -2.4; 87 -2.8; 96 -3.3; 106 -3.9; 116 -4.4; 128 -5.0; 141 -5.3; 155 -5.4; 170 -5.4; 187 -5.5; 206 -5.6; 227 -5.2; 249 -4.4; 274 -3.3; 302 -2.1; 332 -0.9; 365 0.5; 402 1.9; 442 3.4; 486 4.7; 535 5.6; 588 5.9; 647 5.8; 712 5.0; 783 3.7; 861 2.2; 947 0.7; 1042 -0.4; 1146 -1.1; 1261 -1.4; 1387 -1.5; 1526 -1.1; 1678 0.0; 1846 1.1; 2031 2.0; 2234 3.7; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.2; 4788 2.5; 5267 1.6; 5793 4.9; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB50AP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB50AP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.39 | 2.5 dB  |
| Peaking | 174 Hz  | 0.67 | -6.1 dB |
| Peaking | 551 Hz  | 1.7  | 7.8 dB  |
| Peaking | 3207 Hz | 1.7  | 6.9 dB  |
| Peaking | 6221 Hz | 5.67 | 5.2 dB  |
| Peaking | 755 Hz  | 3.66 | 2.1 dB  |
| Peaking | 1344 Hz | 1.44 | -3.0 dB |
| Peaking | 1899 Hz | 2.38 | 0.8 dB  |
| Peaking | 2434 Hz | 6.4  | 2.5 dB  |
| Peaking | 8436 Hz | 3.81 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-XB50AP/Sony%20MDR-XB50AP.png)