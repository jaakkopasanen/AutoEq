# Beats Studio3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.1; 28 1.4; 31 0.8; 34 0.2; 37 -0.3; 41 -0.8; 45 -1.3; 49 -1.7; 54 -2.4; 60 -3.2; 66 -3.8; 72 -4.0; 79 -4.0; 87 -3.8; 96 -3.5; 106 -3.1; 116 -2.7; 128 -2.5; 141 -2.6; 155 -2.8; 170 -3.2; 187 -3.5; 206 -3.8; 227 -4.1; 249 -4.6; 274 -4.9; 302 -5.1; 332 -5.5; 365 -5.6; 402 -4.8; 442 -3.5; 486 -1.9; 535 -0.2; 588 1.0; 647 1.5; 712 0.8; 783 0.6; 861 0.2; 947 -0.2; 1042 0.3; 1146 0.7; 1261 0.6; 1387 0.8; 1526 1.2; 1678 1.4; 1846 1.5; 2031 1.7; 2234 2.6; 2457 3.4; 2703 2.6; 2973 -0.4; 3270 -2.2; 3597 -2.1; 3957 0.6; 4353 3.6; 4788 6.0; 5267 4.9; 5793 4.1; 6373 2.2; 7010 1.3; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -2.4; 11289 -4.7; 12418 -4.8; 13660 -1.8; 15026 -0.4; 16529 -0.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.34 | 4.6 dB  |
| Peaking | 66 Hz    | 0.54 | -5.1 dB |
| Peaking | 316 Hz   | 1.76 | -5.4 dB |
| Peaking | 5096 Hz  | 3    | 6.2 dB  |
| Peaking | 11847 Hz | 3.05 | -5.8 dB |
| Peaking | 415 Hz   | 4.31 | -1.8 dB |
| Peaking | 620 Hz   | 3.3  | 2.4 dB  |
| Peaking | 2556 Hz  | 3.34 | 2.7 dB  |
| Peaking | 2793 Hz  | 0.79 | 2.1 dB  |
| Peaking | 3339 Hz  | 3.01 | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Studio3%20Wireless/Beats%20Studio3%20Wireless.png)