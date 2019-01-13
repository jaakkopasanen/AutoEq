# Razer Man O' War
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 0.0; 23 -0.0; 25 -1.1; 28 -2.5; 31 -3.6; 34 -4.5; 37 -5.1; 41 -5.7; 45 -6.1; 49 -6.4; 54 -6.5; 60 -6.6; 66 -6.7; 72 -6.8; 79 -7.0; 87 -7.2; 96 -7.4; 106 -7.5; 116 -7.6; 128 -7.7; 141 -7.7; 155 -7.6; 170 -7.2; 187 -6.7; 206 -6.3; 227 -7.4; 249 -7.0; 274 -6.2; 302 -5.4; 332 -4.1; 365 -3.4; 402 -3.3; 442 -3.6; 486 -3.1; 535 -1.1; 588 0.4; 647 0.1; 712 -1.3; 783 -1.1; 861 -0.6; 947 -0.2; 1042 0.0; 1146 0.2; 1261 0.6; 1387 0.9; 1526 1.3; 1678 1.0; 1846 1.3; 2031 2.0; 2234 4.3; 2457 3.1; 2703 1.5; 2973 0.6; 3270 1.1; 3597 3.6; 3957 3.1; 4353 -0.6; 4788 -0.4; 5267 -0.7; 5793 -0.6; 6373 -1.6; 7010 0.5; 7711 -2.5; 8482 -6.6; 9330 -5.9; 10263 -1.6; 11289 0.0; 12418 -0.2; 13660 -3.8; 15026 -6.9; 16529 -5.9; 18182 -3.9; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Man O' War GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Man O' War ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 1.11 | -4.7 dB |
| Peaking | 119 Hz   | 0.78 | -6.4 dB |
| Peaking | 260 Hz   | 1.32 | -4.2 dB |
| Peaking | 16037 Hz | 0.86 | -5.7 dB |
| Peaking | 20989 Hz | 1.89 | -4.5 dB |
| Peaking | 3016 Hz  | 0.76 | 3.4 dB  |
| Peaking | 7157 Hz  | 5.28 | 4.0 dB  |
| Peaking | 8787 Hz  | 3.76 | -5.3 dB |
| Peaking | 8876 Hz  | 0.6  | -3.9 dB |
| Peaking | 11494 Hz | 2.01 | 6.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Man%20O'%20War/Razer%20Man%20O'%20War.png)