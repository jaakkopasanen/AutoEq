# MEE audio M9B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -13.8; 23 -13.4; 25 -12.8; 28 -11.6; 31 -10.6; 34 -9.8; 37 -9.2; 41 -8.8; 45 -8.7; 49 -8.7; 54 -8.7; 60 -8.5; 66 -8.3; 72 -7.9; 79 -7.3; 87 -6.8; 96 -6.4; 106 -6.1; 116 -6.0; 128 -5.9; 141 -5.8; 155 -5.6; 170 -5.3; 187 -5.0; 206 -4.5; 227 -4.0; 249 -3.5; 274 -3.1; 302 -2.7; 332 -2.2; 365 -1.6; 402 -1.0; 442 -0.4; 486 0.1; 535 0.7; 588 1.2; 647 1.5; 712 1.4; 783 1.3; 861 0.7; 947 0.1; 1042 0.0; 1146 -0.0; 1261 -0.1; 1387 -0.1; 1526 0.1; 1678 0.1; 1846 0.1; 2031 0.2; 2234 0.7; 2457 0.8; 2703 -1.1; 2973 -3.9; 3270 -6.8; 3597 -8.1; 3957 -7.3; 4353 -6.5; 4788 -5.7; 5267 -6.1; 5793 -8.8; 6373 -14.2; 7010 -11.7; 7711 -5.6; 8482 -3.2; 9330 -7.3; 10263 -11.0; 11289 -7.5; 12418 -2.3; 13660 -3.1; 15026 -8.1; 16529 -10.3; 18182 -10.2; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M9B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-15**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M9B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 168 Hz   | 1.09 | -3.1 dB  |
| Peaking | 6033 Hz  | 1.23 | -10.1 dB |
| Peaking | 10368 Hz | 6.32 | -7.0 dB  |
| Peaking | 19256 Hz | 0.76 | -12.7 dB |
| Peaking | 21 Hz    | 1.17 | -10.8 dB |
| Peaking | 55 Hz    | 0.47 | -6.6 dB  |
| Peaking | 1533 Hz  | 0.35 | 1.3 dB   |
| Peaking | 3502 Hz  | 3.86 | -5.9 dB  |
| Peaking | 5151 Hz  | 7.93 | 3.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M9B/MEE%20audio%20M9B.png)