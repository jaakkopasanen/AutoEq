# Sony MDR-7506

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -3.4; 23 -3.9; 25 -4.4; 28 -5.0; 31 -5.6; 34 -5.9; 37 -6.1; 41 -6.2; 45 -6.2; 49 -6.1; 54 -6.0; 60 -5.8; 66 -5.7; 72 -5.4; 79 -5.2; 87 -5.1; 96 -5.0; 106 -5.0; 116 -4.7; 128 -4.2; 141 -3.7; 155 -3.2; 170 -2.5; 187 -1.6; 206 -0.7; 227 0.7; 249 2.2; 274 1.5; 302 -0.8; 332 -1.6; 365 -1.7; 402 -1.9; 442 -2.0; 486 -1.9; 535 -1.8; 588 -1.6; 647 -1.2; 712 -0.9; 783 -0.7; 861 -0.2; 947 0.0; 1042 -0.1; 1146 -0.5; 1261 -0.8; 1387 -1.3; 1526 -2.0; 1678 -2.8; 1846 -3.5; 2031 -4.3; 2234 -3.9; 2457 -3.5; 2703 -4.4; 2973 -5.6; 3270 -5.5; 3597 -4.6; 3957 -5.2; 4353 -7.6; 4788 -5.3; 5267 -1.3; 5793 1.6; 6373 0.9; 7010 -0.9; 7711 -2.1; 8482 -3.5; 9330 -6.1; 10263 -7.9; 11289 -4.9; 12418 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.48 | -6.5 dB |
| Peaking | 476 Hz   | 3.17 | -1.7 dB |
| Peaking | 2985 Hz  | 0.82 | -4.8 dB |
| Peaking | 4391 Hz  | 6.88 | -4.6 dB |
| Peaking | 22919 Hz | 0.66 | -6.1 dB |
| Peaking | 240 Hz   | 0.76 | -1.8 dB |
| Peaking | 247 Hz   | 2.94 | 5.4 dB  |
| Peaking | 1009 Hz  | 3.06 | 1.2 dB  |
| Peaking | 5973 Hz  | 5.21 | 4.6 dB  |
| Peaking | 10079 Hz | 3.46 | -8.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-7506/Sony%20MDR-7506.png)