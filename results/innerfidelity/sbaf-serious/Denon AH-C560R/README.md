# Denon AH-C560R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.1dB
GraphicEQ: 21 -5.0; 23 -5.3; 25 -5.6; 28 -5.9; 31 -6.2; 34 -6.4; 37 -6.6; 41 -6.8; 45 -7.1; 49 -7.3; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.3; 79 -8.6; 87 -9.0; 96 -9.2; 106 -9.4; 116 -9.4; 128 -9.5; 141 -9.5; 155 -9.5; 170 -9.3; 187 -9.1; 206 -8.8; 227 -8.3; 249 -8.0; 274 -7.4; 302 -6.9; 332 -6.3; 365 -5.7; 402 -5.1; 442 -4.3; 486 -3.8; 535 -3.2; 588 -2.3; 647 -1.7; 712 -1.6; 783 -0.8; 861 -0.4; 947 -0.1; 1042 -0.0; 1146 -0.1; 1261 -0.5; 1387 -1.0; 1526 -1.5; 1678 -1.8; 1846 -1.8; 2031 -1.8; 2234 -2.0; 2457 -2.3; 2703 -3.2; 2973 -3.9; 3270 -3.6; 3597 -2.8; 3957 -3.1; 4353 -5.6; 4788 -7.5; 5267 -8.9; 5793 -8.1; 6373 -5.4; 7010 -3.7; 7711 -4.2; 8482 -6.7; 9330 -5.8; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C560R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.29 | -5.9 dB |
| Peaking | 149 Hz   | 0.64 | -5.3 dB |
| Peaking | 311 Hz   | 1.01 | -3.0 dB |
| Peaking | 5207 Hz  | 1.45 | -8.1 dB |
| Peaking | 8799 Hz  | 6.38 | -5.8 dB |
| Peaking | 990 Hz   | 2.82 | 1.3 dB  |
| Peaking | 3008 Hz  | 1.06 | -2.1 dB |
| Peaking | 3893 Hz  | 3.58 | 3.2 dB  |
| Peaking | 10889 Hz | 5.96 | 1.4 dB  |
| Peaking | 12854 Hz | 1.86 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)