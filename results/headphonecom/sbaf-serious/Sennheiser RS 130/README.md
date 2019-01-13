# Sennheiser RS 130
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.1; 72 3.4; 79 1.9; 87 0.3; 96 -0.8; 106 -2.2; 116 -2.8; 128 -3.4; 141 -4.3; 155 -4.8; 170 -5.0; 187 -5.3; 206 -4.9; 227 -6.0; 249 -5.5; 274 -5.7; 302 -5.5; 332 -5.1; 365 -5.0; 402 -4.5; 442 -4.6; 486 -4.4; 535 -4.2; 588 -2.6; 647 -1.8; 712 -1.2; 783 -1.5; 861 -1.4; 947 -0.6; 1042 0.3; 1146 -0.3; 1261 -2.4; 1387 -4.0; 1526 -5.5; 1678 -5.4; 1846 -5.9; 2031 -4.3; 2234 -2.2; 2457 -0.5; 2703 -4.4; 2973 -7.1; 3270 -6.2; 3597 -7.5; 3957 -4.2; 4353 -11.2; 4788 -8.2; 5267 -5.5; 5793 -6.1; 6373 -5.2; 7010 2.0; 7711 0.3; 8482 -5.2; 9330 -9.6; 10263 -6.1; 11289 -0.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 130 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.47 | 9.7 dB  |
| Peaking | 162 Hz   | 0.42 | -8.5 dB |
| Peaking | 1659 Hz  | 3.73 | -4.6 dB |
| Peaking | 4404 Hz  | 1.04 | -8.1 dB |
| Peaking | 21593 Hz | 2.2  | -6.0 dB |
| Peaking | 1011 Hz  | 1.49 | 3.4 dB  |
| Peaking | 1303 Hz  | 0.49 | -1.9 dB |
| Peaking | 2406 Hz  | 8.19 | 4.6 dB  |
| Peaking | 7252 Hz  | 5.22 | 6.7 dB  |
| Peaking | 9408 Hz  | 4.85 | -9.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20130/Sennheiser%20RS%20130.png)