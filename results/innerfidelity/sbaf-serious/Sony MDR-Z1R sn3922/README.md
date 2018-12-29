# Sony MDR-Z1R sn3922
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.6; 28 -4.8; 31 -4.9; 34 -5.0; 37 -5.0; 41 -4.9; 45 -4.9; 49 -4.8; 54 -4.6; 60 -4.3; 66 -4.0; 72 -4.5; 79 -5.3; 87 -6.0; 96 -6.6; 106 -6.7; 116 -6.6; 128 -6.8; 141 -6.6; 155 -5.7; 170 -5.1; 187 -5.0; 206 -4.3; 227 -3.7; 249 -3.4; 274 -3.1; 302 -2.7; 332 -2.5; 365 -2.2; 402 -1.8; 442 -1.5; 486 -1.4; 535 -0.8; 588 -0.2; 647 -0.1; 712 -0.0; 783 0.2; 861 0.1; 947 0.1; 1042 0.1; 1146 0.3; 1261 0.1; 1387 -0.4; 1526 -1.2; 1678 -1.8; 1846 -2.1; 2031 -1.9; 2234 -1.0; 2457 0.1; 2703 2.7; 2973 1.9; 3270 -3.4; 3597 1.9; 3957 6.0; 4353 6.0; 4788 4.9; 5267 3.9; 5793 3.8; 6373 2.7; 7010 -0.9; 7711 0.4; 8482 -2.9; 9330 -9.1; 10263 -9.1; 11289 -1.7; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1R sn3922 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1R sn3922 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.81 | -4.3 dB  |
| Peaking | 127 Hz   | 0.66 | -6.3 dB  |
| Peaking | 1873 Hz  | 3.37 | -2.6 dB  |
| Peaking | 4632 Hz  | 2.02 | 6.3 dB   |
| Peaking | 9741 Hz  | 4.49 | -11.8 dB |
| Peaking | 2857 Hz  | 6.81 | 6.1 dB   |
| Peaking | 3213 Hz  | 4.89 | -7.3 dB  |
| Peaking | 3797 Hz  | 8.1  | 3.0 dB   |
| Peaking | 3983 Hz  | 6.42 | 1.0 dB   |
| Peaking | 12113 Hz | 7.43 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-Z1R%20sn3922/Sony%20MDR-Z1R%20sn3922.png)