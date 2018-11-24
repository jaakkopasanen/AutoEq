# Bose QuietComfort 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -2.1; 23 -4.0; 25 -5.4; 28 -6.9; 31 -7.9; 34 -8.3; 37 -8.6; 41 -8.6; 45 -8.5; 49 -8.4; 54 -8.3; 60 -8.3; 66 -8.4; 72 -8.5; 79 -8.7; 87 -9.1; 96 -9.3; 106 -9.5; 116 -9.5; 128 -9.3; 141 -8.9; 155 -8.5; 170 -8.3; 187 -8.1; 206 -8.1; 227 -8.1; 249 -7.9; 274 -7.8; 302 -7.8; 332 -7.7; 365 -7.5; 402 -7.1; 442 -6.4; 486 -5.5; 535 -4.4; 588 -3.1; 647 -1.9; 712 -0.6; 783 0.8; 861 1.6; 947 0.7; 1042 -0.5; 1146 -1.5; 1261 -2.5; 1387 -3.6; 1526 -4.9; 1678 -6.6; 1846 -7.7; 2031 -7.8; 2234 -6.8; 2457 -5.3; 2703 -4.4; 2973 -4.4; 3270 -4.9; 3597 -6.6; 3957 -8.8; 4353 -9.1; 4788 -5.1; 5267 -0.8; 5793 -0.4; 6373 -5.9; 7010 -4.8; 7711 -0.5; 8482 -0.3; 9330 -2.8; 10263 -0.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 78 Hz    | 0.31 | -9.4 dB |
| Peaking | 340 Hz   | 1.45 | -4.4 dB |
| Peaking | 1945 Hz  | 2.32 | -7.7 dB |
| Peaking | 4083 Hz  | 2.36 | -8.6 dB |
| Peaking | 22550 Hz | 2.29 | -2.7 dB |
| Peaking | 33 Hz    | 3.89 | -1.4 dB |
| Peaking | 850 Hz   | 4.13 | 3.8 dB  |
| Peaking | 5510 Hz  | 6.1  | 4.1 dB  |
| Peaking | 6445 Hz  | 6.77 | -4.0 dB |
| Peaking | 6723 Hz  | 9.21 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)