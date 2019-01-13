# Sennheiser IE 80 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.5dB
GraphicEQ: 21 -10.4; 23 -10.4; 25 -10.5; 28 -10.5; 31 -10.5; 34 -10.6; 37 -10.6; 41 -10.6; 45 -10.7; 49 -10.8; 54 -10.9; 60 -11.0; 66 -11.1; 72 -11.3; 79 -11.4; 87 -11.6; 96 -11.8; 106 -11.9; 116 -11.9; 128 -11.9; 141 -11.8; 155 -11.6; 170 -11.3; 187 -11.0; 206 -10.6; 227 -10.1; 249 -9.6; 274 -9.1; 302 -8.5; 332 -7.8; 365 -7.2; 402 -6.5; 442 -5.9; 486 -5.2; 535 -4.4; 588 -3.7; 647 -3.0; 712 -2.2; 783 -1.4; 861 -0.8; 947 -0.2; 1042 0.0; 1146 0.0; 1261 0.0; 1387 -0.2; 1526 -0.4; 1678 -0.6; 1846 -0.5; 2031 -0.4; 2234 -0.5; 2457 -0.8; 2703 -1.4; 2973 -2.1; 3270 -2.8; 3597 -3.3; 3957 -4.1; 4353 -5.7; 4788 -8.3; 5267 -8.2; 5793 -3.9; 6373 -0.5; 7010 0.3; 7711 -0.9; 8482 -0.2; 9330 0.0; 10263 0.0; 11289 -0.1; 12418 -1.6; 13660 -1.3; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -0.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 80 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-4**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 80 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 1.1  | -10.2 dB |
| Peaking | 61 Hz    | 0.27 | -9.7 dB  |
| Peaking | 222 Hz   | 0.59 | -5.2 dB  |
| Peaking | 4847 Hz  | 2.95 | -9.0 dB  |
| Peaking | 13002 Hz | 6.2  | -2.0 dB  |
| Peaking | 12 Hz    | 0.32 | 0.2 dB   |
| Peaking | 490 Hz   | 1.83 | -0.9 dB  |
| Peaking | 1007 Hz  | 1.68 | 1.4 dB   |
| Peaking | 3252 Hz  | 3.43 | -1.5 dB  |
| Peaking | 6685 Hz  | 6.8  | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20IE%2080%20S/Sennheiser%20IE%2080%20S.png)