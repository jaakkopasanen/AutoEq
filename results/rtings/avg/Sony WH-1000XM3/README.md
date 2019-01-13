# Sony WH-1000XM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -6.8; 23 -6.7; 25 -6.6; 28 -6.6; 31 -6.6; 34 -6.5; 37 -6.4; 41 -6.2; 45 -6.1; 49 -6.0; 54 -6.0; 60 -6.1; 66 -6.3; 72 -6.6; 79 -6.9; 87 -7.2; 96 -7.5; 106 -7.8; 116 -7.9; 128 -7.8; 141 -7.4; 155 -6.8; 170 -6.0; 187 -5.1; 206 -4.1; 227 -3.3; 249 -2.5; 274 -2.0; 302 -1.6; 332 -1.4; 365 -1.3; 402 -1.4; 442 -1.5; 486 -1.8; 535 -2.0; 588 -2.0; 647 -2.0; 712 -1.1; 783 -0.9; 861 -0.9; 947 -0.3; 1042 0.2; 1146 0.6; 1261 0.3; 1387 -0.2; 1526 -2.2; 1678 -2.9; 1846 -3.2; 2031 -3.8; 2234 -3.3; 2457 -1.5; 2703 -0.0; 2973 -0.0; 3270 0.2; 3597 -0.1; 3957 -0.7; 4353 0.7; 4788 2.5; 5267 0.3; 5793 0.5; 6373 -0.9; 7010 -1.0; 7711 -3.2; 8482 -5.5; 9330 -5.6; 10263 -4.6; 11289 -2.4; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 1.39 | -6.5 dB |
| Peaking | 28 Hz    | 0.5  | -5.2 dB |
| Peaking | 121 Hz   | 0.78 | -6.8 dB |
| Peaking | 1958 Hz  | 3.12 | -4.1 dB |
| Peaking | 9177 Hz  | 2.9  | -6.5 dB |
| Peaking | 606 Hz   | 2.68 | -1.6 dB |
| Peaking | 1281 Hz  | 2.14 | 1.3 dB  |
| Peaking | 1584 Hz  | 6.93 | -2.0 dB |
| Peaking | 4742 Hz  | 6.92 | 3.0 dB  |
| Peaking | 20051 Hz | 4.78 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-1000XM3/Sony%20WH-1000XM3.png)