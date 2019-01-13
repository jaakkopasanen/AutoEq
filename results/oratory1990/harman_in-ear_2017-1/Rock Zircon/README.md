# Rock Zircon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 21 -1.6; 23 -1.9; 25 -2.1; 28 -2.4; 31 -2.7; 34 -2.9; 37 -3.1; 41 -3.4; 45 -3.6; 49 -3.8; 54 -4.1; 60 -4.5; 66 -4.9; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.5; 106 -6.8; 116 -7.1; 128 -7.2; 141 -7.2; 155 -6.9; 170 -5.7; 187 -7.1; 206 -7.1; 227 -6.5; 249 -5.8; 274 -5.0; 302 -4.1; 332 -3.1; 365 -2.3; 402 -1.6; 442 -0.9; 486 -0.3; 535 0.2; 588 0.6; 647 0.9; 712 1.0; 783 1.1; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.8; 1387 -2.3; 1526 -2.7; 1678 -3.1; 1846 -3.1; 2031 -2.6; 2234 -2.0; 2457 -2.3; 2703 -2.6; 2973 -3.3; 3270 -3.0; 3597 -2.4; 3957 -2.0; 4353 -2.6; 4788 -4.5; 5267 -8.2; 5793 -11.9; 6373 -9.2; 7010 -7.7; 7711 -8.2; 8482 -6.2; 9330 -2.7; 10263 -0.2; 11289 0.0; 12418 -4.9; 13660 -17.5; 15026 -27.3; 16529 -29.6; 18182 -26.0; 20000 -17.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Zircon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-11**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Zircon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.1  | -2.2 dB  |
| Peaking | 115 Hz   | 0.82 | -5.7 dB  |
| Peaking | 227 Hz   | 1.8  | -4.1 dB  |
| Peaking | 5811 Hz  | 3.93 | -9.2 dB  |
| Peaking | 17030 Hz | 1.34 | -32.7 dB |
| Peaking | 1926 Hz  | 1.48 | -2.7 dB  |
| Peaking | 7271 Hz  | 2.37 | -2.4 dB  |
| Peaking | 7978 Hz  | 4.59 | -3.5 dB  |
| Peaking | 11577 Hz | 1.53 | 15.7 dB  |
| Peaking | 14586 Hz | 1.8  | -15.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Rock%20Zircon/Rock%20Zircon.png)