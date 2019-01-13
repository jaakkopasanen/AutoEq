# Sony MDR-1000X Wireless NC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 -5.6; 23 -5.3; 25 -5.1; 28 -4.7; 31 -4.4; 34 -4.1; 37 -4.0; 41 -3.8; 45 -3.7; 49 -3.8; 54 -3.9; 60 -4.0; 66 -4.2; 72 -4.4; 79 -4.8; 87 -5.2; 96 -5.6; 106 -5.8; 116 -6.0; 128 -6.2; 141 -6.3; 155 -6.3; 170 -5.8; 187 -5.6; 206 -5.1; 227 -4.4; 249 -4.1; 274 -4.4; 302 -4.0; 332 -3.1; 365 -2.1; 402 -1.8; 442 -2.4; 486 -2.7; 535 -2.6; 588 -0.8; 647 -1.4; 712 -3.4; 783 -0.7; 861 -0.3; 947 -0.4; 1042 0.2; 1146 2.8; 1261 1.4; 1387 0.7; 1526 -1.9; 1678 -3.9; 1846 -5.5; 2031 -5.4; 2234 -4.7; 2457 -2.2; 2703 -0.0; 2973 -1.8; 3270 -2.5; 3597 -2.5; 3957 -5.6; 4353 -7.2; 4788 -4.3; 5267 -4.8; 5793 -7.5; 6373 -5.5; 7010 -1.0; 7711 -2.8; 8482 -5.3; 9330 -5.2; 10263 -2.8; 11289 -1.0; 12418 -0.1; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wireless NC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-29**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wireless NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.68 | -5.3 dB |
| Peaking | 142 Hz   | 0.53 | -6.0 dB |
| Peaking | 1935 Hz  | 4.58 | -5.5 dB |
| Peaking | 5574 Hz  | 0.92 | -5.8 dB |
| Peaking | 22050 Hz | 2.33 | -4.2 dB |
| Peaking | 1070 Hz  | 0.87 | -1.2 dB |
| Peaking | 1184 Hz  | 3.41 | 4.6 dB  |
| Peaking | 6100 Hz  | 6.74 | -3.9 dB |
| Peaking | 6941 Hz  | 3.69 | 4.8 dB  |
| Peaking | 8922 Hz  | 4.14 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wireless%20NC%20Active/Sony%20MDR-1000X%20Wireless%20NC%20Active.png)