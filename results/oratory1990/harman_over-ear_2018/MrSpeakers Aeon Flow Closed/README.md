# MrSpeakers Aeon Flow Closed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.5; 25 1.6; 28 1.9; 31 2.2; 34 2.4; 37 2.6; 41 2.9; 45 3.2; 49 3.5; 54 3.9; 60 4.2; 66 4.2; 72 3.6; 79 3.3; 87 3.5; 96 3.7; 106 3.9; 116 4.3; 128 4.5; 141 4.7; 155 4.9; 170 5.1; 187 4.8; 206 4.4; 227 4.0; 249 3.9; 274 3.8; 302 3.7; 332 3.2; 365 2.9; 402 2.3; 442 2.0; 486 1.9; 535 1.7; 588 1.8; 647 1.7; 712 1.1; 783 0.7; 861 0.2; 947 -0.3; 1042 0.8; 1146 0.8; 1261 1.2; 1387 2.1; 1526 2.5; 1678 3.3; 1846 3.4; 2031 4.6; 2234 4.8; 2457 4.5; 2703 3.8; 2973 6.0; 3270 6.0; 3597 5.7; 3957 5.1; 4353 2.8; 4788 2.3; 5267 -1.2; 5793 -2.0; 6373 1.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.4; 12418 -0.5; 13660 0.0; 15026 0.0; 16529 -0.8; 18182 -2.8; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 49 Hz    | 0.82 | 2.8 dB  |
| Peaking | 184 Hz   | 0.58 | 4.5 dB  |
| Peaking | 2083 Hz  | 1.8  | 3.8 dB  |
| Peaking | 3426 Hz  | 2.38 | 5.6 dB  |
| Peaking | 19389 Hz | 0.98 | -3.8 dB |
| Peaking | 620 Hz   | 5.04 | 0.6 dB  |
| Peaking | 921 Hz   | 5.88 | -1.3 dB |
| Peaking | 4973 Hz  | 3.73 | 2.1 dB  |
| Peaking | 5529 Hz  | 5.18 | -5.5 dB |
| Peaking | 6687 Hz  | 8.43 | 4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Aeon%20Flow%20Closed/MrSpeakers%20Aeon%20Flow%20Closed.png)