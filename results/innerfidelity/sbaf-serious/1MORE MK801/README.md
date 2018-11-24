# 1MORE MK801

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.6; 25 4.0; 28 3.1; 31 2.4; 34 1.8; 37 1.4; 41 0.9; 45 0.4; 49 0.1; 54 -0.2; 60 -0.5; 66 -0.9; 72 -1.2; 79 -1.5; 87 -1.9; 96 -2.1; 106 -2.3; 116 -2.3; 128 -2.6; 141 -2.8; 155 -3.0; 170 -2.6; 187 -2.9; 206 -3.1; 227 -3.1; 249 -3.0; 274 -2.7; 302 -2.0; 332 -1.3; 365 -0.7; 402 -0.0; 442 1.0; 486 1.9; 535 2.2; 588 2.3; 647 2.1; 712 1.3; 783 1.7; 861 2.1; 947 0.6; 1042 -0.2; 1146 -0.0; 1261 0.5; 1387 1.2; 1526 1.8; 1678 2.7; 1846 3.7; 2031 4.4; 2234 4.6; 2457 4.8; 2703 4.6; 2973 4.4; 3270 4.3; 3597 5.0; 3957 4.6; 4353 2.4; 4788 2.7; 5267 5.1; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE MK801 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE MK801 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.95 | 6.1 dB  |
| Peaking | 467 Hz   | 0.23 | -5.3 dB |
| Peaking | 567 Hz   | 0.88 | 7.1 dB  |
| Peaking | 2459 Hz  | 0.82 | 6.9 dB  |
| Peaking | 5902 Hz  | 3.98 | 5.3 dB  |
| Peaking | 853 Hz   | 5.83 | 2.9 dB  |
| Peaking | 894 Hz   | 2.17 | -1.6 dB |
| Peaking | 6712 Hz  | 7.25 | 1.9 dB  |
| Peaking | 7581 Hz  | 2.95 | -1.4 dB |
| Peaking | 10232 Hz | 1.56 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20MK801/1MORE%20MK801.png)