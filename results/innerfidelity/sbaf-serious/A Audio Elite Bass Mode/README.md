# A Audio Elite Bass Mode

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.4; 25 3.9; 28 4.4; 31 4.8; 34 5.1; 37 5.3; 41 5.5; 45 5.7; 49 5.7; 54 5.8; 60 5.9; 66 5.8; 72 5.7; 79 5.6; 87 5.3; 96 4.9; 106 4.5; 116 4.3; 128 4.2; 141 3.7; 155 3.6; 170 3.6; 187 3.5; 206 3.4; 227 3.7; 249 3.9; 274 4.6; 302 4.5; 332 4.8; 365 5.1; 402 4.7; 442 4.0; 486 3.7; 535 3.1; 588 2.6; 647 2.1; 712 2.3; 783 2.5; 861 1.1; 947 0.6; 1042 -0.4; 1146 0.3; 1261 2.1; 1387 3.4; 1526 4.5; 1678 5.6; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`A Audio Elite Bass Mode GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite Bass Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.89 | 0.9 dB  |
| Peaking | 61 Hz    | 0.44 | 5.4 dB  |
| Peaking | 359 Hz   | 1.17 | 4.2 dB  |
| Peaking | 2287 Hz  | 1.12 | 5.9 dB  |
| Peaking | 4969 Hz  | 1.58 | 5.4 dB  |
| Peaking | 1072 Hz  | 5.35 | -2.7 dB |
| Peaking | 1615 Hz  | 4.14 | 1.4 dB  |
| Peaking | 6381 Hz  | 4.47 | 3.5 dB  |
| Peaking | 7514 Hz  | 1.96 | -2.3 dB |
| Peaking | 11415 Hz | 0.86 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20Bass%20Mode/A%20Audio%20Elite%20Bass%20Mode.png)