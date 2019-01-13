# Sony MDR-XB700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 -7.2; 23 -7.4; 25 -7.5; 28 -7.8; 31 -8.0; 34 -8.1; 37 -8.0; 41 -7.7; 45 -7.6; 49 -7.5; 54 -7.4; 60 -8.2; 66 -9.2; 72 -9.9; 79 -10.6; 87 -11.1; 96 -11.5; 106 -11.8; 116 -11.7; 128 -11.6; 141 -11.7; 155 -11.1; 170 -11.1; 187 -10.6; 206 -9.9; 227 -9.1; 249 -8.1; 274 -6.6; 302 -5.5; 332 -4.4; 365 -3.6; 402 -2.8; 442 -1.7; 486 -0.7; 535 0.5; 588 1.6; 647 3.2; 712 4.4; 783 4.4; 861 2.8; 947 1.3; 1042 -0.8; 1146 -2.5; 1261 -4.2; 1387 -5.9; 1526 -7.2; 1678 -8.0; 1846 -8.5; 2031 -8.3; 2234 -7.0; 2457 -4.2; 2703 -1.5; 2973 2.0; 3270 4.3; 3597 -0.0; 3957 -2.2; 4353 -1.1; 4788 -1.6; 5267 -1.7; 5793 -6.6; 6373 -4.4; 7010 1.5; 7711 0.3; 8482 -4.7; 9330 -7.2; 10263 -3.5; 11289 -0.1; 12418 0.0; 13660 -0.0; 15026 -0.8; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.28 | -7.4 dB |
| Peaking | 151 Hz   | 0.89 | -8.6 dB |
| Peaking | 1819 Hz  | 2.5  | -9.7 dB |
| Peaking | 9250 Hz  | 4.3  | -7.8 dB |
| Peaking | 22050 Hz | 2.23 | -4.2 dB |
| Peaking | 740 Hz   | 2.44 | 6.3 dB  |
| Peaking | 1333 Hz  | 3.93 | -3.0 dB |
| Peaking | 2257 Hz  | 7.45 | -2.7 dB |
| Peaking | 3196 Hz  | 6.9  | 5.9 dB  |
| Peaking | 5956 Hz  | 9.09 | -8.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)