# Apple AirPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 4.6; 45 3.2; 49 2.0; 54 0.7; 60 -0.5; 66 -1.4; 72 -2.0; 79 -2.4; 87 -2.7; 96 -2.9; 106 -3.0; 116 -3.0; 128 -2.9; 141 -2.8; 155 -2.6; 170 -2.4; 187 -2.3; 206 -2.1; 227 -1.9; 249 -1.8; 274 -1.7; 302 -1.6; 332 -1.6; 365 -1.6; 402 -1.6; 442 -1.5; 486 -1.4; 535 -1.2; 588 -1.1; 647 -0.8; 712 -0.3; 783 0.1; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.8; 1261 -1.8; 1387 -3.1; 1526 -4.7; 1678 -5.9; 1846 -6.8; 2031 -7.1; 2234 -6.3; 2457 -5.3; 2703 -5.0; 2973 -4.6; 3270 -4.1; 3597 -4.0; 3957 -4.3; 4353 -4.9; 4788 -5.0; 5267 -5.5; 5793 -5.7; 6373 -4.6; 7010 -4.0; 7711 -4.5; 8482 -5.8; 9330 -6.4; 10263 -4.5; 11289 -2.3; 12418 -4.2; 13660 -7.8; 15026 -6.1; 16529 -0.4; 18182 0.0; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple AirPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple AirPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.95 | 7.3 dB  |
| Peaking | 1943 Hz  | 1.9  | -6.0 dB |
| Peaking | 6402 Hz  | 0.52 | -5.1 dB |
| Peaking | 14067 Hz | 3.88 | -7.0 dB |
| Peaking | 20214 Hz | 3.82 | -3.5 dB |
| Peaking | 42 Hz    | 2.06 | 4.4 dB  |
| Peaking | 106 Hz   | 0.38 | -3.2 dB |
| Peaking | 938 Hz   | 2.91 | 1.7 dB  |
| Peaking | 9153 Hz  | 8.26 | -2.3 dB |
| Peaking | 17392 Hz | 2.82 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Apple%20AirPods/Apple%20AirPods.png)