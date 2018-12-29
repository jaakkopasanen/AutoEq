# Sony MDR-7520
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.2dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.4; 28 3.1; 31 1.9; 34 0.9; 37 -0.1; 41 -1.2; 45 -2.2; 49 -3.1; 54 -4.0; 60 -5.0; 66 -5.7; 72 -6.2; 79 -6.8; 87 -7.3; 96 -7.9; 106 -7.9; 116 -7.8; 128 -7.4; 141 -6.5; 155 -5.9; 170 -5.3; 187 -3.3; 206 -2.3; 227 -1.5; 249 -0.2; 274 0.6; 302 0.1; 332 0.9; 365 0.4; 402 0.0; 442 -0.2; 486 -0.5; 535 -0.4; 588 0.1; 647 0.3; 712 0.2; 783 0.4; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -1.0; 1387 -2.1; 1526 -3.5; 1678 -5.0; 1846 -6.3; 2031 -8.1; 2234 -8.5; 2457 -7.3; 2703 -6.3; 2973 -4.1; 3270 -2.3; 3597 0.8; 3957 5.4; 4353 6.0; 4788 6.0; 5267 5.3; 5793 2.8; 6373 4.4; 7010 2.5; 7711 -0.7; 8482 -8.3; 9330 -11.1; 10263 -7.1; 11289 -0.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-71**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.81 | 6.9 dB   |
| Peaking | 98 Hz   | 0.95 | -8.7 dB  |
| Peaking | 2384 Hz | 1.49 | -11.6 dB |
| Peaking | 4772 Hz | 0.92 | 8.6 dB   |
| Peaking | 9181 Hz | 3.48 | -14.7 dB |
| Peaking | 162 Hz  | 3.96 | -2.0 dB  |
| Peaking | 285 Hz  | 1.83 | 2.0 dB   |
| Peaking | 1017 Hz | 1.27 | 1.4 dB   |
| Peaking | 2158 Hz | 1.47 | -2.2 dB  |
| Peaking | 2403 Hz | 5.25 | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7520/Sony%20MDR-7520.png)