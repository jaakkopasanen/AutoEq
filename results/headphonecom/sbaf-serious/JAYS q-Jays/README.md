# JAYS q-Jays

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.3; 25 1.3; 28 1.2; 31 1.1; 34 0.9; 37 0.9; 41 0.8; 45 0.7; 49 0.5; 54 0.3; 60 -0.0; 66 -0.2; 72 -0.3; 79 -0.7; 87 -1.0; 96 -1.3; 106 -1.5; 116 -1.8; 128 -1.8; 141 -2.1; 155 -2.4; 170 -2.6; 187 -2.7; 206 -2.6; 227 -2.6; 249 -2.4; 274 -2.4; 302 -2.0; 332 -1.7; 365 -1.8; 402 -1.9; 442 -1.6; 486 -1.2; 535 -0.9; 588 -0.4; 647 -0.2; 712 0.0; 783 0.2; 861 0.3; 947 0.2; 1042 -0.0; 1146 -0.1; 1261 -0.1; 1387 -0.4; 1526 -1.2; 1678 -2.0; 1846 -2.0; 2031 -1.6; 2234 -0.8; 2457 0.6; 2703 3.1; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.8; 9330 -5.7; 10263 -1.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS q-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS q-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 192 Hz   | 0.87 | -2.7 dB |
| Peaking | 421 Hz   | 2.02 | -1.1 dB |
| Peaking | 1974 Hz  | 1.35 | -7.4 dB |
| Peaking | 3676 Hz  | 0.54 | 8.4 dB  |
| Peaking | 9118 Hz  | 3.36 | -8.8 dB |
| Peaking | 26 Hz    | 1.02 | 1.4 dB  |
| Peaking | 3037 Hz  | 6.85 | 2.0 dB  |
| Peaking | 3756 Hz  | 1.12 | -0.8 dB |
| Peaking | 6058 Hz  | 5.76 | 1.7 dB  |
| Peaking | 14552 Hz | 1.95 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20q-Jays/JAYS%20q-Jays.png)