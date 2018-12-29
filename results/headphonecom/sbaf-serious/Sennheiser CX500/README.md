# Sennheiser CX500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.1; 23 -7.1; 25 -7.2; 28 -7.2; 31 -7.2; 34 -7.2; 37 -7.3; 41 -7.4; 45 -7.5; 49 -7.7; 54 -7.9; 60 -8.1; 66 -8.3; 72 -8.6; 79 -8.9; 87 -9.0; 96 -9.2; 106 -9.3; 116 -9.3; 128 -9.4; 141 -9.5; 155 -9.5; 170 -9.4; 187 -9.2; 206 -8.9; 227 -8.6; 249 -8.2; 274 -7.8; 302 -7.2; 332 -6.6; 365 -5.8; 402 -5.2; 442 -4.7; 486 -4.2; 535 -3.4; 588 -2.6; 647 -1.9; 712 -1.2; 783 -0.7; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.1; 1261 0.2; 1387 0.1; 1526 -0.3; 1678 -0.3; 1846 -0.1; 2031 0.4; 2234 1.1; 2457 2.2; 2703 3.4; 2973 4.7; 3270 5.9; 3597 6.0; 3957 5.1; 4353 2.5; 4788 0.3; 5267 -1.6; 5793 -6.7; 6373 -4.7; 7010 0.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -1.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 27 Hz    |  0.18 | -6.7 dB |
| Peaking | 148 Hz   |  0.64 | -5.1 dB |
| Peaking | 307 Hz   |  0.96 | -3.5 dB |
| Peaking | 3448 Hz  |  2.08 | 6.7 dB  |
| Peaking | 5925 Hz  |  5.97 | -9.0 dB |
| Peaking | 520 Hz   |  2.58 | -0.9 dB |
| Peaking | 961 Hz   |  0.92 | 0.9 dB  |
| Peaking | 1729 Hz  |  2.95 | -1.1 dB |
| Peaking | 7265 Hz  | 10.54 | 1.8 dB  |
| Peaking | 10213 Hz | 10.36 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX500/Sennheiser%20CX500.png)